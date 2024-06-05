import pytest
import os
from Qart import Qrcode

def test_qrcode(tmpdir):
    Qr = Qrcode("蒹葭蒼蒼")
    Qr.generate(2, "L", mask = 0, mode = "Normal")
    Qr.show()
    temp_file = tmpdir.join("test.png")
    Qr.save(str(temp_file))
    assert os.path.exists(str(temp_file))
    Qr.save(str(temp_file), 2, 20)
    assert os.path.exists(str(temp_file))
    



    