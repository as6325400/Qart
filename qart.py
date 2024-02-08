from qrcode import Qrcode
import numpy as np
import math
from img import Img

class Qart(Qrcode, Img):
    
    def __init__(self, Text):
        super().__init__(Text)
        return
        
    def generate(self, path: str, version: int, error_correction: str, mask: int = 0, mode = "Normal"):
        self._Qrcode__dataload(version, error_correction, mask, mode)
        self.Binaryimage = Img.image2moudlebase((version * 4 + 17), path=path)
        self.__QartHandler(mode, mask=mask)
    
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
                    rebuildtable[i][j] = self.GetColor(i, j)
                    continue
                if self.GetMask(i, j, self.mask) == self.GetBinaryImage(i, j):
                    rebuildtable[i][j] = 0
                else:
                    rebuildtable[i][j] = 1
        redata = [" "] * len(self._Encode__code)
        print("redatalen", len(redata))
        cc = 0
        for i in range(len(dataTable)):
            for j in range(len(dataTable)):
                
                if dataTagTable[i][j] != 1 and dataTagTable[i][j] != 2:
                    continue
                cc += 1
                # print(dataTable[i][j], self.order[dataTable[i][j]])
                redata[self.order[dataTable[i][j]]] = str(rebuildtable[i][j])
        
        print("cc", cc)
        redatacode = "".join(redata)
        redatacode = redatacode.replace(" ", "")
        print("redata", len(redatacode))
        
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
        # self._Qrcode__SetMask()
        
        return self.QR