class NameOfClas():
    class_attribute = 'value'
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def method(self):
        return self.param1 + self.param2

    @classmethod
    def class_method(cls, param1, param2):
        return cls(param1, param2)
    
    @staticmethod
    def static_method(param1, param2):
        return param1 + param2
    
