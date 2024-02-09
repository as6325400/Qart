# A package to blend image and Qrcode

## Install

```py
pip install Qart
```

## Usage

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
    - The third parameter is the version of the mask. (option)
    - The fourth parameter is the mode of the positioning point. (option)

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
    To create an object where the constructor takes a string that you want to encode

    ```py
    from Qart import Qart

    Qr = Qart("Accepted")
    ```

2. **Generate**
    - The first parameter is the path of the image to be merged.
    - The second parameter is the version of the QR code to be generated.
    - The third parameter is the error correction level of the QR code to be generated.
    - The fourth parameter is the version of the mask. (option)
    - The fifth parameter is the mode of the positioning point. (option)

    ```py
    Qr.generate("img.png", 6, "L", mask = 0, mode = "Normal")
    ```

3. **Show**
    Show QRcode use matplotlib

    ```py
    Qr.show()
    ```

