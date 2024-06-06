import pytest
import os
from Qart import Qart
import shutil

def test_qrcode(tmpdir):
    Qr = Qart('accept')
     # 资源目录中的文件路径
    resource_dir = "tests"
    resource_file = "img2.jpeg"
    resource_path = os.path.join(resource_dir, resource_file)
    temp_file = tmpdir.join(resource_file)
    shutil.copy(resource_path, str(temp_file))
    Qr.generate(temp_file, 20, "L", mask = 0, mode = "Normal")
    Qr.show()
    



    