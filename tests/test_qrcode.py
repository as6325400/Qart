import unittest
from Qart.qart import Qrcode
from Qart.Error import EncodeError
import shutil
import os
import tempfile
from unittest.mock import patch


class TestQrcode(unittest.TestCase):
    @patch('matplotlib.pyplot.imsave')
    def test_qrcodesave(self, mock_plt_save):
        resource_dir = "tests"
        resource_file = "1.png"
        resource_path = os.path.join(resource_dir, resource_file)

        self.assertTrue(os.path.exists(resource_path), f"Resource file {resource_path} does not exist")

        with tempfile.TemporaryDirectory() as tmpdirname:
            temp_file = os.path.join(tmpdirname, resource_file)

            shutil.copy(resource_path, temp_file)

            with tempfile.NamedTemporaryFile(suffix=".png", delete=True) as temp_output_file:
                Qr = Qrcode("Accepted")
                Qr.generate(6, "L", mask = 0, mode = "Normal")
                Qr = Qrcode("1234")
                Qr.generate(6, "L", mask = 1, mode = "Micro")
                Qr = Qrcode("12345")
                Qr.generate(6, "L", mask = 2, mode = "Normal")
                Qr = Qrcode("/O.O/")
                Qr.generate(6, "H", mask = 3, mode = "Normal")
                Qr = Qrcode("謝")
                Qr.generate(6, "M", mask = 4, mode = "Normal")
                Qr = Qrcode("Accepted")
                Qr.generate(6, "Q", mask = 5, mode = "Normal")
                Qr.save("test.jpg")
                Qr = Qrcode("Accepted")
                Qr.generate(6, "M", mask = 6, mode = "Normal")
                Qr.save("test.png")
                Qr = Qrcode("Accepted")
                Qr.generate(6, "Q", mask = 7, mode = "Normal")
                num = Qr.InformationMask()
                Qr.save()
                self.assertEqual(mock_plt_save.call_count, 3)
            with tempfile.NamedTemporaryFile(suffix=".png", delete=True) as temp_output_file:
                Qr = Qrcode("Acceptedwadawdqawdewrwareawerwarewd")
                Qr.generate(20, "L", mask = 0, mode = "Normal")
                
    @patch('matplotlib.pyplot.show')
    def test_qrcode_data_show(self, mock_plt_show):
        Qr = Qrcode("Accepted")
        Qr.generate(6, "Q", mask = 7, mode = "Normal")
        num = Qr.InformationMask()
        Qr.showdata()
        self.assertEqual(mock_plt_show.call_count, 1)
        
    @patch('matplotlib.pyplot.show')
    def test_qrcode_show(self, mock_plt_show):
        Qr = Qrcode("Accepted")
        Qr.generate(6, "Q", mask = 7, mode = "Normal")
        Qr.show()
        self.assertEqual(mock_plt_show.call_count, 1)
        
    def test_qrcode_tp_numpy(self):
        Qr = Qrcode("Accepted")
        Qr.generate(6, "Q", mask = 7, mode = "Normal")
        Qr.to_numpy()
    def test_encode_error(self):
        with self.assertRaises(EncodeError):
            Qr = Qrcode("한")
            Qr.generate(6, "L", mask = 0, mode = "Normal")
            
    def test_value_error(self):
        with self.assertRaises(ValueError):
            Qr = Qrcode("dwadw")
            Qr.generate(50, "L", mask = 0, mode = "Normal")
        
if __name__ == '__main__':
    unittest.main()