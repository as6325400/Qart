import unittest
from Qart.img import Image
import shutil
import os
import tempfile
from unittest.mock import patch


class TestImage(unittest.TestCase):
     @patch('matplotlib.pyplot.imsave')
     def test_imgsave(self, mock_plt_save):
          resource_dir = "tests"
          resource_file = "1.png"
          resource_path = os.path.join(resource_dir, resource_file)

          self.assertTrue(os.path.exists(resource_path), f"Resource file {resource_path} does not exist")
          with tempfile.TemporaryDirectory() as tmpdirname:
               temp_file = os.path.join(tmpdirname, resource_file)


               shutil.copy(resource_path, temp_file)

               with tempfile.NamedTemporaryFile(suffix=".png", delete=True) as temp_output_file:

                    img = Image(temp_file)
                    img.SetModuleNums(20)

                    img.save(temp_output_file.name, mode="Modulebase")
                    img.save(temp_output_file.name, mode="RGB")
                    img.save(temp_output_file.name, mode="Grayscale")
                    img.save(mode="OTSU")

                    self.assertEqual(mock_plt_save.call_count, 4)
               with tempfile.NamedTemporaryFile(suffix=".jpg", delete=True) as temp_output_file:
                    img = Image(temp_file)
                    img.SetModuleNums(20)

                    img.save(temp_output_file.name, mode="Modulebase")
                    img.save(temp_output_file.name, mode="RGB")
                    img.save(temp_output_file.name, mode="Grayscale")
                    img.save(mode="OTSU")

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
          self.assertEqual(mock_plt_show.call_count, 4)

          
if __name__ == '__main__':
     unittest.main()