import baselib

class MyClass(baselib.MyBaseClass):
    def __init__(self):
        pass
    
    def Sum(self, a, b):
        return a + b
    
    def WrongSum(self, a, b):
        return a + 2*b
