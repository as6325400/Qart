import pytest
import os
from Qart import Image
import shutil

def test_img(tmpdir):
     # 资源目录中的文件路径
    resource_dir = "tests"
    resource_file = "1.png"
    resource_path = os.path.join(resource_dir, resource_file)
    
    # 确保资源文件存在 
    assert os.path.exists(resource_path), f"Resource file {resource_path} does not exist"
    
    # 将资源文件复制到临时目录中
    temp_file = tmpdir.join(resource_file)
    shutil.copy(resource_path, str(temp_file))

    # 创建 Image 对象并使用临时文件路径
    img = Image(str(temp_file))
    img.SetModuleNums(20)
    img.save(mode = "Modulebase")