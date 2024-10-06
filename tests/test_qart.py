import unittest
from Qart.qart import Qart
import shutil
import os
import tempfile
from unittest.mock import patch


class TestQart(unittest.TestCase):
    @patch('matplotlib.pyplot.imsave')
    def test_Qartsave(self, mock_plt_save):
        # 资源目录中的文件路径
        resource_dir = "tests"
        resource_file = "1.png"
        resource_path = os.path.join(resource_dir, resource_file)

        # 确保资源文件存在
        self.assertTrue(os.path.exists(resource_path), f"Resource file {resource_path} does not exist")

        # 创建临时目录
        with tempfile.TemporaryDirectory() as tmpdirname:
            temp_file = os.path.join(tmpdirname, resource_file)

            # 将资源文件复制到临时目录中
            shutil.copy(resource_path, temp_file)

            # 使用 NamedTemporaryFile 创建临时保存路径
            with tempfile.NamedTemporaryFile(suffix=".png", delete=True) as temp_output_file:
                Qr = Qart("Accepted")
                Qr.generate(resource_path, 6, "L", mask = 0, mode = "Normal")
                # # 创建 Image 对象并使用临时文件路径
                # img = Image(temp_file)
                # img.SetModuleNums(20)

                # 保存到临时文件路径，文件会在测试结束后自动删除
                Qr.save()
                self.assertEqual(mock_plt_save.call_count, 1)
            with tempfile.NamedTemporaryFile(suffix=".png", delete=True) as temp_output_file:
                Qr = Qart("Acceptedwadawdqawdewrwareawerwarewd")
                Qr.generate(resource_path, 10, "L", mask = 0, mode = "Normal")

        
if __name__ == '__main__':
    unittest.main()