from encode import Encode
from canvas import Canvas
import numpy as np
from Table import VersionTable, NormalLocationPoint, AlignmentPatternTable, ECCFomatSiteTable, ECCFomatTable, VersionBitTable
from time import sleep


class Qrcode(Encode, Canvas):
    __versionTable = VersionTable
    __NormalLocationPoint = NormalLocationPoint
    __AlignmentPatternTable = AlignmentPatternTable
    __ECCFormatTable = ECCFomatTable
    __VersionBitTable = VersionBitTable
    
    def __init__(self, Text):
        super().__init__(Text)
        
    
    def generate(self, version: int, error_correction: str, mask: int = 0, mode = "Normal"):
        self.ECCFomatSiteTable = ECCFomatSiteTable(version)
        self.size = version * 4 + 17
        self.QRDataAttribute = np.zeros((self.size, self.size), dtype = np.uint8)
        
        
        self._Encode__generate(version, error_correction)
        self._Canvas__resize(Qrcode.__versionTable[str(version)]["moudles"])
        self.__QrcodeHandler(mode, mask=mask)
        
    def __SetPositionPattern(self, mode = "Normal"):
        shift = self.size - 7
        PointSet = []
        
        if mode == "Normal":
            PointSet = Qrcode.__NormalLocationPoint
            
        for i in PointSet:
            if i[2] == 1:
                self.SetBlack(i[0], i[1])
                self.SetBlack(i[0] + shift, i[1])
                self.SetBlack(i[0], i[1] + shift)
            else:
                self.SetWhite(i[0], i[1])
                self.SetWhite(i[0] + shift, i[1])
                self.SetWhite(i[0], i[1] + shift)
    
    def __SetSeparatorPattern(self):
        for i in range(8):
            self.SetWhite(7, i)
            self.SetWhite(i, 7)
            self.SetWhite(self.size - 8, i)
            self.SetWhite(i, self.size - 8)
            self.SetWhite(7, self.size - 1 - i)
            self.SetWhite(self.size - 1 - i, 7)
        return
    
    def __SerBlackMoudle(self):
        self.SetBlack(4 * self.version + 9, 8)
        return
    
    def __SetTimingPattern(self):
        for i in range(8, self.size - 8):
            if i % 2 == 0:
                self.SetBlack(6, i)
                self.SetBlack(i, 6)
            else:
                self.SetWhite(6, i)
                self.SetWhite(i, 6)
        return
    
    def __SetAlignmentPattern(self):
        for i in Qrcode.__AlignmentPatternTable[str(self.version)]:
            for j in Qrcode.__AlignmentPatternTable[str(self.version)]:
                for k in range(-2, 3):
                    for l in range(-2, 3):
                        if i < 7 and j < 7: continue
                        elif i > self.size - 8 and j < 7: continue
                        elif i < 7 and j > self.size - 8: continue
                        if k == 0 and l == 0:
                            self.SetBlack(i, j)
                        elif k == -2 or k == 2 or l == -2 or l == 2:
                            self.SetBlack(i + k, j + l)
                        else:
                            self.SetWhite(i + k, j + l)
        return
    
    def __SetVersionPattern(self):
        if self.version < 7: return
        versionBit = Qrcode.__VersionBitTable[self.version]
        
        idx = 0
        for i in range(5, -1, -1):
            for j in range(self.size - 9, self.size - 12, -1):
                self.SetBlack(i, j) if versionBit[idx] == "1" else self.SetWhite(i, j)
                self.SetBlack(j, i) if versionBit[idx] == "1" else self.SetWhite(j, i)
                idx += 1
        
        return
    
    def __SetFormatPattern(self, ECC: str, mask: int):
        self.mask = mask
        self.format = ""
        if ECC == "L":
            self.format = "01"
        elif ECC == "M":
            self.format = "00"
        elif ECC == "Q":
            self.format = "11"
        elif ECC == "H":
            self.format = "10"
        self.format += format(mask, 'b').zfill(3)
        for i in self.ECCFomatSiteTable:
            x, y = i.split(',')
            x, y = int(x), int(y)
            if ECCFomatTable[self.format][self.ECCFomatSiteTable[i]] == "1":
                self.SetBlack(x, y)
            else:
                self.SetWhite(x, y)
        return
    
    def __SetDataPattern(self):
        data = self._Encode__code
        length = self.version * 4 + 17
        cc = 0
        count = 0
        flag = 0
        for i in range(length - 1, -1, -2):
            if flag == 0:
                for j in range(length - 1, -1, -1):
                    for k in range(i, i - 2, -1):
                        if self.QR[j][k] != 128:
                            continue
                        if data[count] == "1":
                            self.SetBlack(j, k)
                        else:
                            self.SetWhite(j, k)
                        self.QRDataAttribute[j][k] = 10
                        count += 1
                flag = (flag + 1) % 2
            else:
                for j in range(0, length, 1):
                    for k in range(i, i - 2, -1):
                        if self.QR[j][k] != 128:
                            continue
                        if data[count] == "1":
                            self.SetBlack(j, k)
                        else:
                            self.SetWhite(j, k)
                        self.QRDataAttribute[j][k] = 10
                        count += 1
                flag = (flag + 1) % 2
            if i == 8:
                i -= 1
                
        return
    
    def __SetMask(self):
        length = self.version * 4 + 17
        for i in range(length):
            for j in range(length):
                if self.QRDataAttribute[i][j] == 10:
                    bit : int = 1
                    if self.mask == 0:
                        if (i + j) % 2 == 0: bit = 0
                    elif self.mask == 1:
                        if i % 2 == 0: bit = 0
                    elif self.mask == 2:
                        if j % 3 == 0: bit = 0
                    elif self.mask == 3:
                        if (i + j) % 3 == 0: bit = 0
                    elif self.mask == 4:
                        if (i // 2 + j // 3) % 2 == 0: bit = 0
                    elif self.mask == 5:
                        if (i * j) % 2 + (i * j) % 3 == 0: bit = 0
                    elif self.mask == 6:
                        if ((i * j) % 2 + (i * j) % 3) % 2 == 0: bit = 0
                    elif self.mask == 7:
                        if ((i + j) % 2 + (i * j) % 3) % 2 == 0: bit = 0
                    
                    old = 1
                    if self.QR[i][j] == 0:
                        old = 0
                    color = old ^ bit
                    self.SetBlack(i, j) if color == 1 else self.SetWhite(i, j)
    
        return
        
    
    def __QrcodeHandler(self, mode = "Normal", mask = 0):
        
        self.__SetPositionPattern(mode)
        self.__SetSeparatorPattern()
        self.__SerBlackMoudle()
        self.__SetTimingPattern()
        self.__SetAlignmentPattern()
        self.__SetVersionPattern()
        self.__SetFormatPattern(self.ECC, mask)
        self.__SetDataPattern()
        self.__SetMask()
        
        ## Set Black point
        
        
        ## Set Black point
        return self.QR
    
    



    



