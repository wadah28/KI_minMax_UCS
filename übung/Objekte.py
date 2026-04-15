class Hund:
    def __init__(self, name , alter):
        self.name = name
        self.alter = alter
    def bellen(self):
        return "WUFF"
    def info(self):
        return f"Hundname: {self.name} , alter: {self.alter} , typ {self.__class__.__name__}"
class Ente:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    def bellen(self):
        return "WAK"
    def info(self):
        return f"Tiername: {self.name} , alter: {self.alter} , typ {self.__class__.__name__}"

class Roboter:
    def __init__(self,name , alter):
        self.name = name
        self.alter = alter
    def bellen(self):
        return "KOKO KAKA"
    def info(self):
        return f"Robotername: {self.name} , alter: {self.alter} , typ {self.__class__.__name__}"
