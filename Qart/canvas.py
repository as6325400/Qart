import numpy as np
import matplotlib.pyplot as plt

class Canvas:
    
    def __init__(self):
        return
        
    def __resize(self, size: int):
        self.QR = np.full((size, size), dtype=int, fill_value=128)
        self.size = size
        self.version = (size - 21) // 4 + 1
        return
    
    def SetBlack(self, x: int, y: int):
        if(x < 0 or x >= len(self.QR) or y < 0 or y >= len(self.QR)):
            raise ValueError("The coordinate is out of range")
        self.QR[x][y] = 0
        return
    
    def SetWhite(self, x: int, y: int):
        if(x < 0 or x >= len(self.QR) or y < 0 or y >= len(self.QR)):
            raise ValueError("The coordinate is out of range")
        self.QR[x][y] = 255
        return
    
    def GetColor(self, x: int, y: int):
        if(x < 0 or x >= len(self.QR) or y < 0 or y >= len(self.QR)):
            raise ValueError("The coordinate is out of range")
        return 0 if self.QR[x][y] == 0 else 1
    
    def show(self):
        plt.imshow(self.QR, cmap='gray')  # 'cmap' 參數控制著色映射，'gray' 表示灰階
        plt.colorbar()  # 顯示色條
        plt.show()
    