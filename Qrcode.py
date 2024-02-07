from encode import Encode



class Qrcode(Encode):

    def __init__(self, Text):
        super().__init__(Text)
        return
    
    def generate(self, version: int, error_correction: str):
        self._Encode__generate(version, error_correction)
    
    



    

q = Qrcode("YEECY")
q.generate(1, "Q")



