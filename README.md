# A package to blend image and Qrcode
[![codecov](https://codecov.io/gh/as6325400/Qart/branch/main/graph/badge.svg)](https://codecov.io/gh/as6325400/Qart)

## Package Features Showcase

<p float="left">
  <img src="https://github.com/user-attachments/assets/75c42f5a-4a15-440e-a36f-2f4681643862" width="30%" />
  <img src="https://github.com/user-attachments/assets/b84dd1a7-48ca-4595-ad4e-bf29f401f860" width="30%" />
  <img src="https://github.com/user-attachments/assets/cd1013ec-dec4-468b-a88f-cd215ec2be85" width="30%" />
</p>
<p float="left">
  <img src="https://github.com/user-attachments/assets/9dc1e827-957e-41b7-9884-198898f4346c" width="30%" />
  <img src="https://github.com/user-attachments/assets/64fcd718-97a8-4ace-9fbc-f1a97e0552f6" width="30%" />
  <img src="https://github.com/user-attachments/assets/0ad633dd-915b-4b1c-912f-99dceb05ec17" width="30%" />
</p>




## Install

```py
pip install Qart
```

## Usage

### InformationMask

if object inherit Qrcode can use this method

Return a numpy array sizeof module nums


1. if Mask[i][j] == 0，this point is cannot be changed
2. if Mask[i][j] == 1，this point is dont care
3. if Mask[i][j] == 2，this point is padding
4. if Mask[i][j] == 3，this point is data
5. if Mask[i][j] == 4，this point is ecc
6. if Mask[i][j] == 5，this point remain bits


in short, if mask[i][j] == [1, 2, 4], this point can change

### Qrcode

1. **Create Object**
    To create an object where the constructor takes a string that you want to encode

    ```py
    from Qart import Qrcode

    Qr = Qrcode("Accepted")
    ```

2. **Generate**
    - The first parameter is the version of the QR code to be generated.
    - The second parameter is the error correction level of the QR code to be generated.
    - The third parameter is the version of the mask 0 ~ 7. (option)
    - The fourth parameter is the mode of the positioning point can use "Normal" and "Micro". (option)

    ```py
    Qr.generate(6, "L", mask = 0, mode = "Normal")
    ```

3. **Show**
    Show QRcode use matplotlib

    ```py
    Qr.show()
    ```

### Qart 

1. **Create Object**
    To create an object where the constructor takes a string or numpy array that you want to encode

    ```py
    from Qart import Qart
    Qr = Qart("Accepted")
    ```

2. **Generate**
    - The first parameter is the path of the image to be merged.
    - The second parameter is the version of the QR code to be generated.
    - The third parameter is the error correction level of the QR code to be generated.
    - The fourth parameter is the version of the mask 0 ~ 7. (option)
    - The fifth parameter is the mode of the positioning point can use "Normal" and "Micro". (option)

    ```py
    Qr.generate("img.png", 6, "L", mask = 0, mode = "Normal")
    ```

3. **Show**
    Show QRcode use matplotlib

    ```py
    Qr.show()
    ```

### Image

1. **Load Image**
   ```py
   from Qart import Image
   img = Image("1.png")
   ```
3. **Set Moudlenums (option)**
   ```py
   from Qart import Image
   img.SetModuleNums(MoudleNums: int)
   ```
4. **Show**
   Four mode, "RGB" "Grayscale" "OTSU" "Modulebase"
            
   ```py
   from Qart import Image
   img.show("OTSU")
   ```

## Reference

1. [QArt Codes](https://research.swtch.com/qart)
2. [thonky](https://www.thonky.com/qr-code-tutorial/)
