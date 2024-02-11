from .qrcode import Qrcode
import numpy as np
import math
from .img import Img
import cv2
from matplotlib import pyplot as plt
from .Error import *

class Qart(Qrcode, Img):
    
    def __init__(self, arg):
        super().__init__(arg)
        return
    
    def generate(self, path: str, version: int, error_correction: str, mask: int = 0, mode = "Normal"):
        self._Qrcode__dataload(version, error_correction, mask, mode)
        self.Binaryimage = Img.image2moudlebase((version * 4 + 17), path=path)
        return self.__QartHandler(mode, mask=mask)
    
    def GetBinaryImage(self, i, j):
        return 0 if self.Binaryimage[i][j] == 0 else 1
    
    def __BlendImage(self):
        dataTable = self.QRdataBits
        dataTagTable = self.tagTable
        rebuildtable = np.full((len(dataTable), len(dataTable)), dtype=int, fill_value=-1)
        
        for i in range(len(dataTable)):
            for j in range(len(dataTable)):
                if dataTable[i][j] < 0:
                    continue
                if dataTagTable[i][j] != 1:
                    rebuildtable[i][j] = (self.GetColor(i, j) + 1) % 2
                    continue
                if self.GetMask(i, j, self.mask) == self.GetBinaryImage(i, j):
                    rebuildtable[i][j] = 0
                else:
                    rebuildtable[i][j] = 1
        redata = [" "] * len(self._Encode__code)
        
        # test = np.full((len(dataTable), len(dataTable)), dtype=int, fill_value=128)
        # for i in range(len(dataTable)):
        #     for j in range(len(dataTable)):
        #         test[i][j] = 0 if rebuildtable[i][j] == 0 else 255
                
        # plt.imshow(test, cmap='gray')  # 'cmap' 參數控制著色映射，'gray' 表示灰階
        # plt.show()
        # print("datatable[40][40]", dataTable[40][40])
        # print("dataTagtable[40][40]", dataTagTable[40][40])
        # print("color[40][40]", self.GetColor(40, 40))
        # print("rebuild[40][40]", rebuildtable[40][40])
        cc = 0
        tag = []
        for i in range(len(dataTable)):
            for j in range(len(dataTable)):
                
                # 只要 padding 跟 data 有關的就要處理
                if dataTagTable[i][j] != 1 and dataTagTable[i][j] != 2:
                    continue
                # cc += 1
                # if(dataTagTable[i][j] == 2):
                #     tag.append(self.order[dataTable[i][j]])
                # print(dataTable[i][j], self.order[dataTable[i][j]])
                if rebuildtable[i][j] < 0:
                    raise ValueError("The data is not complete")
                # if self.order[dataTable[i][j]] == 0:
                #     # print(i, j)
                redata[self.order[dataTable[i][j]]] = str(rebuildtable[i][j])
        redatacode = "".join(redata)
        redatacode = redatacode.replace(" ", "")
        # print("redatacode", len(redatacode), redatacode)
        self._Encode__block__encode(self.version, self.ECC, redatacode)
        self._Encode__remainder_bits(self.version, self.ECC)
        return
        
    
    def __QartHandler(self, mode = "Normal", mask = 0):
        
        self._Qrcode__SetPositionPattern(mode)
        self._Qrcode__SetSeparatorPattern()
        self._Qrcode__SerBlackMoudle()
        self._Qrcode__SetTimingPattern()
        self._Qrcode__SetAlignmentPattern()
        self._Qrcode__SetVersionPattern()
        self._Qrcode__SetFormatPattern(self.ECC, mask)
        self._Qrcode__SetDataPattern()
        self.__BlendImage()
        self._Qrcode__SetDataPattern()
        self._Qrcode__SetMask()
        return self.QR