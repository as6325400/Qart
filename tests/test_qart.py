import unittest
from Qart.qart import Qart
import shutil
import os
import tempfile
from unittest.mock import patch


class TestQart(unittest.TestCase):
    @patch('matplotlib.pyplot.imsave')
    def test_Qartsave(self, mock_plt_save):
        resource_dir = "tests"
        resource_file = "1.png"
        resource_path = os.path.join(resource_dir, resource_file)
        self.assertTrue(os.path.exists(resource_path), f"Resource file {resource_path} does not exist")

        with tempfile.TemporaryDirectory() as tmpdirname:
            temp_file = os.path.join(tmpdirname, resource_file)

            shutil.copy(resource_path, temp_file)

            with tempfile.NamedTemporaryFile(suffix=".png", delete=True) as temp_output_file:
                Qr = Qart("Accepted")
                Qr.generate(resource_path, 6, "L", mask = 0, mode = "Normal")
                Qr.save()
                self.assertEqual(mock_plt_save.call_count, 1)
            with tempfile.NamedTemporaryFile(suffix=".png", delete=True) as temp_output_file:
                Qr = Qart("Acceptedwadawdqawdewrwareawerwarewd")
                Qr.generate(resource_path, 10, "L", mask = 0, mode = "Normal")

        
if __name__ == '__main__':
    unittest.main()