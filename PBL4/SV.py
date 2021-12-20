class SinhVien:
    # thuộc tính
    Masv = ""
    Namesv = ""
    Diemdanh = True
    URLhinhanh = ""
    # phương thức
    def __init__(self,_Masv="",_Namesv="",_Diemdanh=True,_URLhinhanh = ""):
        self.Masv = _Masv;
        self.Namesv = _Namesv;
        self.Diemdanh = _Diemdanh;
        self.URLhinhanh = _URLhinhanh;
    def setMasv(self,_Masv):
        self.Masv = _Masv
    def getMasv(self):
        return self.Masv
    def setNamesv(self,_Namesv):
        self.Namesv = _Namesv
    def getNamesv(self):
        return self.Namesv
    def setDiemdanh(self,_Diemdanh):
        self.Diemdanh = _Diemdanh
    def getDiemdanh(self):
        return self.Diemdanh
    def setURLhinhanh(self,_URLhinhanh):
        self.URLhinhanh=_URLhinhanh
    def getURLhinhanh(self):
        return self.URLhinhanh
def ChangeToSV(data):
    sv = SinhVien()
    sv.Masv = str(data[0])
    sv.Namesv = str(data[1])
    sv.Diemdanh = data[2]
    sv.URLhinhanh = str(data[3])
    return sv