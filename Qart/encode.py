from .Error import *
from .Table import VersionTable, ModeIndicatorTable, PerBlockTable
import reedsolo as rs

rs.init_tables(0x11D)

class Encode:
    __NUMERIC_MODE = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    __ALPHANUMERIC_MODE = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
                           'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15, 'G' : 16, 'H' : 17, 'I' : 18, 'J' : 19,
                           'K' : 20, 'L' : 21, 'M' : 22, 'N' : 23, 'O' : 24, 'P' : 25, 'Q' : 26, 'R' : 27, 'S' : 28, 'T' : 29,
                           'U' : 30, 'V' : 31, 'W' : 32, 'X' : 33, 'Y' : 34, 'Z' : 35, ' ' : 36, '$' : 37, '%' : 38, '*' : 39,
                           '+' : 40, '-' : 41, '.' : 42, '/' : 43, ':' : 44}
    __ISO_IEC_8859_1_BYTE_MODE = {}
    
    __versionTable = VersionTable
    
    __mode_indicator_table = ModeIndicatorTable
    
    __per_block = PerBlockTable
    
    __prim = rs.find_prime_polys(c_exp=8, fast_primes=False, single=True)
    
    
    rs.init_tables(c_exp=8, prim=__prim)

    def __init__(self, Text):
        self.__Text = Text
        self.__EncodeMode = ""
        self.__EncodeText = ""
        self.__mode_indicator = ""
        self.__char_length_indicator = ""
        self.__terminator = ""
        self.__code = ""
        self.__padding = ""
        self.StartPadding: int
        self.StartEcc: int
        if self.__EncodeModeController() != True:
            raise EncodeError("The text is not valid")
        return
    
    def __NumericEncodeMode(self):
        # Clear any previously encoded text
        self.__EncodeText = ""

        # Iterate through the text, processing three characters at a time
        for i in range(0, len(self.__Text), 3):
            group = self.__Text[i:i+3]

            # Convert the group of characters into binary
            binary = format(int(group), 'b').zfill(10)

            # Handle the case where the last group of characters is less than three
            if i + 3 > len(self.__Text):
                if len(group) == 1:
                    binary = binary[6:]
                elif len(group) == 2:
                    binary = binary[3:]

            # Directly append the binary string to the encoded text
            self.__EncodeText += binary

        return self.__EncodeText

    def __AlphanumericEncodeMode(self):
        # Clear any previously encoded text
        self.__EncodeText = ""
        group = [self.__ALPHANUMERIC_MODE[c] for c in self.__Text]
        for i in range(0, len(group), 2):
            if len(group) - i == 1:
                self.__EncodeText += format(group[i], 'b').zfill(6)
            else:
                self.__EncodeText += format((group[i] * 45) + group[i+1], 'b').zfill(11)
        
        return self.__EncodeText
    
    def __ISO_IEC_8859_1_BYTE_MODE(self):
        # Clear any previously encoded text
        self.__EncodeText = ""
        for char in self.__Text:
            self.__EncodeText += format(ord(char), 'b').zfill(8)
        return self.__EncodeText
    
    # def __kanjiEncodeMode(self):

    def __EncodeModeController(self):
        if self.__Text.isdigit():
            self.__EncodeMode = "Numeric"
            self.__NumericEncodeMode()
            return True
        
        elif all(c in self.__ALPHANUMERIC_MODE for c in self.__Text):
            self.__EncodeMode = "Alphanumeric"
            self.__AlphanumericEncodeMode()
            return True
        
        elif all(0 <= ord(char) <= 255 for char in self.__Text):
            # ISO/IEC 8859-1
            self.__EncodeMode = "Byte"
            self.__ISO_IEC_8859_1_BYTE_MODE()
            return True

        return False
    
    def GetText(self):
        return self.__Text
    
    def __GetEncodeText(self):
        return self.__EncodeText
    
    def GetEncodeMode(self):
        return self.__EncodeMode
    
    def __character_count_indicator(self, version: int, mode: str):
        if version < 1 or version > 40:
            raise ValueError("Version must be between 1 and 40")
        if mode not in ["Numeric", "Alphanumeric", "Byte", "Kanji"]:
            raise ValueError("Mode must be Numeric, Alphanumeric, Byte, or Kanji")
        if version >= 1 and version <= 9:
            if mode == "Numeric": return 10
            if mode == "Alphanumeric": return 9
            if mode == "Byte": return 8
            if mode == "Kanji": return 8
        elif version >= 10 and version <= 26:
            if mode == "Numeric": return 12
            if mode == "Alphanumeric": return 11
            if mode == "Byte": return 16
            if mode == "Kanji": return 10
        elif version >= 27 and version <= 40:
            if mode == "Numeric": return 14
            if mode == "Alphanumeric": return 13
            if mode == "Byte": return 16
            if mode == "Kanji": return 12
    
    def __error_correction(self, number_list: list):
        nsym = Encode.__per_block[str(self.version)][str(self.ECC)]["num_ecc"]
        # pregen isn't fastly enough
        # self.gen = rs.rs_generator_poly_all(len(number_list) + nsym)
        mesecc = rs.rs_encode_msg(number_list, nsym, gen = rs.rs_generator_poly(nsym))
        integers = [b for b in mesecc]
        integers = integers[len(number_list):]
        return integers
    
    def __binary_to_int(self, binary: str):
        
        if len(binary) % 8 != 0:
            raise ValueError("binary length must be a multiple of 8")
        
        return [int(binary[i:i+8], 2) for i in range(0, len(binary), 8)]
    
    def __block__encode(self, version: int, ECC: str, code: str):
        self.__code = code
        paddingLength = len(self.__padding) // 8
        temp = self.__binary_to_int(self.__code)
        # print(temp)
        int_code = []
        for i in range(len(temp)):
            int_code.append({
                "idx": i,
                "data": temp[i]
                })
        tag = ['d' if i < len(int_code) - paddingLength else 'p' for i in range(len(int_code))]
        # print(len(tag))
        PerBlock = PerBlockTable[str(version)][ECC]
        
        if(len(int_code) != PerBlock["num_dc_per_block_g1"] * PerBlock["num_block_g1"] + PerBlock["num_dc_per_block_g2"] * PerBlock["num_block_g2"]):
            raise ValueError("The length of the data code is not correct")
        
        temp_data = []
        temp_ecc = []
        temp_tag = []
        temp_merge_tag = []
        idx = 0
        for num_blocks, block_size in [(PerBlock["num_block_g1"], PerBlock["num_dc_per_block_g1"]), 
                                    (PerBlock["num_block_g2"], PerBlock["num_dc_per_block_g2"])]:
            for _ in range(num_blocks):
                temp_data.append(int_code[idx:idx + block_size])
                temp_tag.append(tag[idx:idx + block_size])
                idx += block_size
                
        for i in temp_data:
            temp_ecc.append(self.__error_correction([j["data"] for j in i]))
            
        temp_merge = []
        
        for i in range(max(PerBlock["num_dc_per_block_g1"], PerBlock["num_dc_per_block_g2"])):
            for j in range(len(temp_data)):
                if i < len(temp_data[j]):
                    temp_merge.append(temp_data[j][i])
                    temp_merge_tag.append(temp_tag[j][i])
                else:
                    continue
                
        for i in range(PerBlock["num_ecc"]):
            for j in range(len(temp_ecc)):
                temp_merge.append({
                    "idx": len(temp_merge),
                    "data": temp_ecc[j][i]
                    }
                )
                temp_merge_tag.append('e')
        
        # print(temp_merge)
        self.__code = "".join(format(num['data'], '08b') for num in temp_merge)
        self.__tag = "".join(item * 8 for item in temp_merge_tag)
        self.order = []
        
        for i in temp_merge:
            for j in range(8):
                self.order.append(i["idx"] * 8 + j)
                
        # print(len(self.__code), len(self.__tag))
        # print(self.__tag)
        
    def __remainder_bits(self, version: int, ECC: str):
        version_to_zeros = {
            range(2, 7): 7,
            range(14, 21): 3,
            range(21, 28): 4,
            range(28, 35): 3,
        }

        # print("old order len", len(self.order))
        
        for version_range, zeros in version_to_zeros.items():
            if self.version in version_range:
                # print("zero", zeros)
                self.__code += "0" * zeros
                self.__tag += "r" * zeros
                for _ in range(zeros):
                    self.order.append(self.order[-1] + 1)
                    # print(self.order[-1])
                break  
        
    
    def __generate(self, version: int, ECC: str):
        self.version = version
        self.ECC = ECC
        if version < 1 or version > 40:
            raise ValueError("Version must be between 1 and 40")
        
        if ECC not in ["L", "M", "Q", "H"]:
            raise ValueError("ECC must be L, M, Q, or H")
        
        table = Encode.__versionTable[str(version)]["ECC"][ECC]
        
        if len(self.GetText()) > table[self.GetEncodeMode()]:
            raise ValueError("Input data too large for specified version and ECC")
         
        self.__mode_indicator = Encode.__mode_indicator_table[self.GetEncodeMode()]
        self.__char_length_indicator = format(len(self.GetText()), 'b').zfill(self.__character_count_indicator(version, self.GetEncodeMode()))
        self.__code = self.__mode_indicator + self.__char_length_indicator + self.__GetEncodeText()
        
        if table["databits"] - len(self.__code) >= 4:
            self.__terminator = "0000"
        
        elif table["databits"] - len(self.__code) >= 2:
            self.__terminator = "00"
        
        self.__code += self.__terminator 
        
        if table["databits"] - len(self.__code) > 0:
            
            if len(self.__code) % 8 != 0:
                self.__padding = "0" * (8 - (len(self.__code) % 8))
            
            
            paddingTable = "1110110000010001"
            paddingNeed = table["databits"] - len(self.__code) - len(self.__padding)
            
            self.__padding += (paddingNeed // 16) * paddingTable
            self.__padding += paddingTable[:paddingNeed % 16]
        
        self.__code += self.__padding
        # print("origin", len(self.__code))
        ################################### block ###################################
        # print("origin", len(self.__code), self.__code)
        self.__block__encode(version, ECC, self.__code)
        
        ################################### block ###################################
        
        ################################### remainder bits ###################################
        
        self.__remainder_bits(version, ECC)
        # print(self.order)
        # print("new order len", len(self.order))
        ################################### remainder bits ###################################
        
        
        
        
        
        

    
       

# Qrcode("1").generate()
# Qrcode("12303").generate()
# Qrcode("01917875412").generate()
# Qrcode("/O.O/").generate()
# Qrcode("HELLO WORLD").generate()
# Qrcode("ISO/IEC 18004:2015").generate()
# Qrcode("APTX4869").generate()
# Qrcode("QR Code").generate()
# Qrcode("Yeecy").generate()
# Qrcode("Hello, world! «(°ö° )¬").generate()
