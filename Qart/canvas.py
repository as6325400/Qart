import numpy as np
import matplotlib.pyplot as plt
import time

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
        
                 
    def save(self, filename: str = "", padding: int = 0, module_size: int = 8):
        if(filename == ""):
            filename = time.strftime("%Y%m%d%H%M%S", time.localtime())
        if(filename[-4:] == ".png"):
            filename = filename[:-4]
        if(filename[-4:] == ".jpg"):
            filename = filename[:-4]
        pixel_num = (self.size + padding * 2) * module_size
        image = np.full((pixel_num, pixel_num), dtype=int, fill_value=255)
        for i in range(self.size):
            for j in range(self.size):
                if(self.QR[i][j] == 0):
                    image[(i + padding) * module_size: (i + padding + 1) * module_size, (j + padding) * module_size: (j + padding + 1) * module_size] = 0
        plt.imsave(filename + ".png", image, cmap='gray')
        return
    
    def to_numpy(self, module_size: int = 8, padding: int = 0):
        pixel_num = (self.size) * module_size + padding * 2
        image = np.full((pixel_num, pixel_num), dtype=int, fill_value=255)
        for i in range(self.size):
            for j in range(self.size):
                if(self.QR[i][j] == 0):
                    image[(i) * module_size + padding: (i + 1) * module_size + padding, (j) * module_size + padding: (j + 1) * module_size + padding] = 0
        return image
    
    
    