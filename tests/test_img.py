import unittest
from Qart.img import Image
import shutil
import os
import tempfile
from unittest.mock import patch


class TestImage(unittest.TestCase):
     @patch('matplotlib.pyplot.imsave')
     def test_imgsave(self, mock_plt_save):
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
                    # 创建 Image 对象并使用临时文件路径
                    img = Image(temp_file)
                    img.SetModuleNums(20)

                    # 保存到临时文件路径，文件会在测试结束后自动删除
                    img.save(temp_output_file.name, mode="Modulebase")
                    img.save(temp_output_file.name, mode="RGB")
                    img.save(temp_output_file.name, mode="Grayscale")
                    img.save(mode="OTSU")

                    # 确保 save() 调用了4次
                    self.assertEqual(mock_plt_save.call_count, 4)
               with tempfile.NamedTemporaryFile(suffix=".jpg", delete=True) as temp_output_file:
                    # 创建 Image 对象并使用临时文件路径
                    img = Image(temp_file)
                    img.SetModuleNums(20)

                    # 保存到临时文件路径，文件会在测试结束后自动删除
                    img.save(temp_output_file.name, mode="Modulebase")
                    img.save(temp_output_file.name, mode="RGB")
                    img.save(temp_output_file.name, mode="Grayscale")
                    img.save(mode="OTSU")

                    # 确保 save() 调用了4次
                    self.assertEqual(mock_plt_save.call_count, 8)

     @patch('matplotlib.pyplot.show')
     def test_imgshow(self, mock_plt_show):
          resource_dir = "tests"
          resource_file = "1.png"
          resource_path = os.path.join(resource_dir, resource_file)
          self.assertTrue(os.path.exists(resource_path), f"Resource file {resource_path} does not exist")
          img = Image(resource_path)
          img.SetModuleNums(20)
          img.show()
          img.show("Grayscale")
          img.show("OTSU")
          img.show("Modulebase")

          # 确保 plt.show() 被调用过
          self.assertEqual(mock_plt_show.call_count, 4)

          
if __name__ == '__main__':
     unittest.main()