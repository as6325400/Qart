from .encode import Encode
from .canvas import Canvas
import numpy as np
from .Table import VersionTable, NormalLocationPoint, AlignmentPatternTable, ECCFomatSiteTable, ECCFomatTable, VersionBitTable, MicroLocationPoint, LocationPointMask
import matplotlib.pyplot as plt


class Qrcode(Encode, Canvas):
    __versionTable = VersionTable
    __NormalLocationPoint = NormalLocationPoint
    __MicroLocationPoint = MicroLocationPoint
    __AlignmentPatternTable = AlignmentPatternTable
    __ECCFormatTable = ECCFomatTable
    __VersionBitTable = VersionBitTable
    __LocationMask = LocationPointMask
    
    def __init__(self, Text):
        super().__init__(Text)
        
    def __dataload(self, version: int, error_correction: str, mask: int = 0, mode = "Normal"):
        self.ECCFomatSiteTable = ECCFomatSiteTable(version)
        self.size = version * 4 + 17
        self._Encode__generate(version, error_correction)
        self._Canvas__resize(Qrcode.__versionTable[str(version)]["moudles"])
        self.QRdataBits = np.full((self.size,  self.size), dtype=int, fill_value=-1)
        self.QRdataRole = np.full((self.size,  self.size), dtype=int, fill_value=0)
        self.Mask = np.full((self.size, self.size), dtype=int, fill_value=0)
        # 0 是整個非定位區域
        # 1 是定位點
        # 2 是分隔符
        # 3 是黑色模塊
        # 4 是定時模塊
        # 5 是對齊模塊
        # 6 是版本模塊
        # 7 是格式模塊
        
        # mask 中
        # 0 為不可更改
        # 1 為 dont care
        
        
    def generate(self, version: int, error_correction: str, mask: int = 0, mode = "Normal"):
        self.__dataload(version, error_correction, mask, mode)
        self.__QrcodeHandler(mode, mask=mask)
        return self.QR
        
    def __SetPositionPattern(self, mode = "Normal"):
        shift = self.size - 7
        PointSet = []
        
        if mode == "Normal":
            PointSet = Qrcode.__NormalLocationPoint
        elif mode == "Micro":
            PointSet = Qrcode.__MicroLocationPoint
            
        for i in PointSet:
            if i[2] == 1:
                self.QRdataRole[i[0]][i[1]] = 1
                self.QRdataRole[i[0] + shift][i[1]] = 1
                self.QRdataRole[i[0]][i[1] + shift] = 1
                self.SetBlack(i[0], i[1])
                self.SetBlack(i[0] + shift, i[1])
                self.SetBlack(i[0], i[1] + shift)
            else:
                self.QRdataRole[i[0]][i[1]] = 1
                self.QRdataRole[i[0] + shift][i[1]] = 1
                self.QRdataRole[i[0]][i[1] + shift] = 1
                self.SetWhite(i[0], i[1])
                self.SetWhite(i[0] + shift, i[1])
                self.SetWhite(i[0], i[1] + shift)
                
        for i in Qrcode.__LocationMask:
            # dont care
            if i[2] == 0:
                self.Mask[i[0] + shift][i[1]] = 1
                self.Mask[i[0]][i[1] + shift] = 1
                self.Mask[i[0]][i[1]] = 1
    
    def __SetSeparatorPattern(self):
        for i in range(8):
            self.QRdataRole[7][i] = 2
            self.QRdataRole[i][7] = 2
            self.QRdataRole[self.size - 8][i] = 2
            self.QRdataRole[i][self.size - 8] = 2
            self.QRdataRole[7][self.size - 1 - i] = 2
            self.QRdataRole[self.size - 1 - i][7] = 2
            self.SetWhite(7, i)
            self.SetWhite(i, 7)
            self.SetWhite(self.size - 8, i)
            self.SetWhite(i, self.size - 8)
            self.SetWhite(7, self.size - 1 - i)
            self.SetWhite(self.size - 1 - i, 7)
        return
    
    def __SerBlackMoudle(self):
        self.QRdataRole[4 * self.version + 9][8] = 3
        self.SetBlack(4 * self.version + 9, 8)
        return
    
    def __SetTimingPattern(self):
        for i in range(8, self.size - 8):
            self.Mask[i][6] = 1
            self.Mask[6][i] = 1
            if i % 2 == 0:
                self.QRdataRole[6][i] = 4
                self.QRdataRole[i][6] = 4
                self.SetBlack(6, i)
                self.SetBlack(i, 6)
            else:
                self.QRdataRole[6][i] = 4
                self.QRdataRole[i][6] = 4
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
                        ## dont care
                        self.Mask[i + k][j + l] = 1
                        if k == 0 and l == 0:
                            self.QRdataRole[i][j] = 5
                            self.SetBlack(i, j)
                        elif k == -2 or k == 2 or l == -2 or l == 2:
                            self.QRdataRole[i + k][j + l] = 5
                            self.SetBlack(i + k, j + l)
                        else:
                            self.QRdataRole[i + k][j + l] = 5
                            self.SetWhite(i + k, j + l)
        return
    
    def __SetVersionPattern(self):
        if self.version < 7: return
        versionBit = Qrcode.__VersionBitTable[self.version]
        
        idx = 0
        for i in range(5, -1, -1):
            for j in range(self.size - 9, self.size - 12, -1):
                self.QRdataRole[i][j] = 6
                self.QRdataRole[j][i] = 6
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
                self.QRdataRole[x][y] = 7
                self.SetBlack(x, y)
            else:
                self.QRdataRole[x][y] = 7
                self.SetWhite(x, y)
        return
    
    def __SetDataPattern(self):
        data = self._Encode__code
        # print("code", data)
        length = self.version * 4 + 17
        count = 0
        flag = 0
        self.tagTable = np.full((length, length), dtype=int, fill_value=0)
        # tagTable 為 1 表示此點為 padding
        # tagTable 為 2 表示此點為 data
        # tagTable 為 3 表示此點為 ecc
        # tagTable 為 4 表示此點為 remain bits
        tag_values = {"p": 1, "d": 2, "e": 3, "r": 4}
        # print(len(self._Encode__tag), len(data))
        idx = [i for i in range(length - 1, -1, -2)]
        idx = idx[:len(idx) - 4]
        idx += [5, 3, 1]
        # print(len(data), len(idx))
        
        cc = 0
        for i in idx:
            # print(i)
            if flag == 0:
                for j in range(length - 1, -1, -1):
                    for k in range(i, i - 2, -1):
                        if self.QRdataRole[j][k] != 0:
                            continue
                        if data[count] == "1":
                            self.SetBlack(j, k)
                        else:
                            self.SetWhite(j, k)
                        cc += 1
                        self.QRdataBits[j][k] = count
                        self.tagTable[j][k] = tag_values[self._Encode__tag[count]]
                        self.Mask[j][k] = tag_values[self._Encode__tag[count]] + 1
                        # self.show()
                        count += 1
                flag = (flag + 1) % 2
            else:
                for j in range(0, length, 1):
                    for k in range(i, i - 2, -1):
                        if self.QRdataRole[j][k] != 0:
                            continue
                        if data[count] == "1":
                            self.SetBlack(j, k)
                        else:
                            self.SetWhite(j, k)
                        cc += 1
                        self.QRdataBits[j][k] = count
                        self.tagTable[j][k] = tag_values[self._Encode__tag[count]]
                        self.Mask[j][k] = tag_values[self._Encode__tag[count]] + 1
                        # self.show()
                        count += 1
                flag = (flag + 1) % 2
                
        # print("cc", cc, count)
        # for i in range(length):
        #     for j in range(length):
        #         print(f"{self.QRdataBits[i][j]:08d}", end="     ")
        #     print()
            
            
            
        # print()
        # print()
        # print()
        # print()
        # print()
        # print()
        # print()
        # print()
        # print()
        # print()
        # print()
        return
    
    def GetMask(self, i: int, j: int, mask: int):
        if i < 0 or i >= self.size or j < 0 or j >= self.size:
            raise ValueError("The coordinate is out of range")
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
        return bit
    
    def __SetMask(self):
        length = self.version * 4 + 17
        for i in range(length):
            for j in range(length):
                if self.QRdataBits[i][j] >= 0:
                    bit = self.GetMask(i, j, self.mask)
                    old = self.GetColor(i, j)
                    self.SetBlack(i, j) if old ^ bit == 1 else self.SetWhite(i, j)
        return
        
    def showdata(self):
        temp = np.full((self.size, self.size), dtype=int, fill_value=128)
        
        for i in range(len(self.tagTable)):
            for j in range(len(self.tagTable)):
                if self.tagTable[i][j] == 2:
                    temp[i][j] = 255
        temp[0][0] = 0
        plt.imshow(temp, cmap='gray')
        plt.colorbar()
        plt.show()
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
        
        return self.QR
    
    def InformationMask(self):
        return self.mask
    
    



    



