from Qart import Qrcode
from Qart import Qart

Q = Qrcode("Accept")
Q.generate(1, "L", 0, "Normal")
Q.show()

Q = Qart("Accept")
Q.generate("1.png", 1, "L")
Q.show()