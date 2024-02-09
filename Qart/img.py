import cv2
import numpy as np
import sys
import math
import matplotlib.pyplot as plt


class Img:
    @classmethod
    def read(cls, path):
        return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    
    @classmethod
    def Grayscale(cls, img):
        grayscale_img = np.empty(img.shape[:-1])  # 假設 img 是 (高, 寬, 3)
        grayscale_img = np.dot(img[...,:3], [0.299, 0.587, 0.114]).round().astype(np.int32)
        return grayscale_img
    
    @classmethod
    def OTSU(cls, img_luminance):
        img_luminance = img_luminance.astype(np.uint8)
        histogram = np.zeros(256)
        for i in range(img_luminance.shape[0]):
            for j in range(img_luminance.shape[1]):
                histogram[img_luminance[i][j]] += 1
        distribution = histogram / np.sum(histogram)

        best_threshold = 0
        minimum_variance = sys.maxsize

        for threshold in range(256):
            # calculate mean
            # --------------
            # lower than threshold
            sum_low = 0
            for i in range(threshold):
                sum_low += distribution[i] * i
            mean_low = sum_low / np.sum(distribution[:threshold])

            # higher than threshold
            sum_high = 0
            for i in range(threshold, 256):
                sum_high += distribution[i] * i
            mean_high = sum_high / np.sum(distribution[threshold:])

            # calculate variance
            # ------------------
            # lower
            variance_low = 0
            for i in range(threshold):
                variance_low += (mean_low - i)**2 * distribution[i]

            # higher
            variance_high = 0
            for i in range(threshold, 256):
                variance_high += (mean_high - i)**2 * distribution[i]

            # sum up
            group_in_variance = variance_low + variance_high

            if group_in_variance < minimum_variance:
                best_threshold = threshold
                minimum_variance = group_in_variance

        _, binarized_img = cv2.threshold(
            img_luminance, best_threshold, 255, cv2.THRESH_BINARY)
        return binarized_img, best_threshold, minimum_variance

    @classmethod
    def module_based_binarization(cls, img, modulenums):
        
        module_size = Img.__calculateMoudleSize(len(img), modulenums)
        img_size = img.shape[0]
        subimage_size = module_size
        binary_img = np.zeros(
            (img.shape[0] // module_size, img.shape[1] // module_size), dtype=np.uint8)

        # 自己建立Gaussian kernel
        gaussian_kernel = np.zeros((subimage_size, subimage_size))
        center = (subimage_size - 1) // 2
        sigma = 1

        # 設定Gaussian kernel內各個i, j的值
        for i in range(subimage_size):
            for j in range(subimage_size):
                gaussian_kernel[i][j] = 1/(2*math.pi*sigma**2) * \
                    np.exp(-((i-center)**2 + (j-center)**2) / 2*sigma**2)

        # 讓此kernel的總和為1
        gaussian_kernel /= np.sum(gaussian_kernel)

        # 計算各個subimage的binarization的結果後
        # assign給整個subimage，即Module
        for i in range(img_size // subimage_size):
            for j in range(img_size // subimage_size):
                region = img[i*subimage_size:(i+1)*subimage_size,
                             j*subimage_size:(j+1)*subimage_size]
                value = np.round(np.sum(region * gaussian_kernel) / 255)
                binary_img[i][j] = value * 255
        
        if modulenums > len(binary_img):
            ## copilot 寫的 不知道能不能動
            ## 要把圖片放大時在下方及右方補 0
            binary_img = np.pad(binary_img, ((0, modulenums - len(binary_img)), (0, 0)), 'constant', constant_values=(255))      
        else:
            binary_img = binary_img[:modulenums, :modulenums]
        return binary_img
    
    @classmethod
    def __calculateMoudleSize(cls, img_size, qrMoudlesize):
        return img_size // qrMoudlesize
    
    @classmethod
    def image2moudlebase(cls, moudlesnum, path: str):
        image = Img.read(path)
        image = Img.Grayscale(image)
        image = Img.OTSU(image)[0]
        image = Img.module_based_binarization(image, moudlesnum)
        return image
    
class Image(Img):
    def __init__(self, path: str):
        self.path = path
        self.image = self.read(path)
        self.grayscale = self.Grayscale(self.image)
        self.otsu = self.OTSU(self.grayscale)[0]
        self.modulebase = self.module_based_binarization(self.otsu, 50)
        return
    
    def SetModuleNums(self, moudlesnum):
        self.modulebase = self.module_based_binarization(self.otsu, moudlesnum)
        return
    
    def show(self, mode = "RGB"):
        if mode == "RGB":
            plt.imshow(self.image)
        elif mode == "Grayscale":
            plt.imshow(self.grayscale, cmap='gray')
        elif mode == "OTSU":
            plt.imshow(self.otsu, cmap='gray')
        elif mode == "Modulebase":
            plt.imshow(self.modulebase, cmap='gray')
        plt.show()