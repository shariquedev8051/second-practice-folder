from icecream import ic
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa


# class SingleTone:
#     """SingleTone class"""
#     def __new__(cls):
#         """Responsible for creation of new object"""
#         if not hasattr(cls, "instance"):
#             cls.instance = super().__new__(cls)
#         return cls.instance

# s1 = SingleTone()
# s2 = SingleTone()
# print(id(s1),id(s2))

# ========================================================
'''
class Form:
    html = ""
    def get_html(self):
        return self.html

class Text(Form):
    html = '<input type = "text" value= "Dummy Data Text">'

class Email(Form):
    html = '<input type = "email" value= "Dummy Data Email">'

class Password(Form):
    html = '<input type = "password" value= "Dummy Data Password">'


# Methode 2 using eval methode
class FormFactory():
    def create_form(self, inp):
        l = ["Text","Password",'Email']
        inp = inp.title()
        if inp in l:
           obj = eval(inp)()
           return obj.get_html()
        else:
            print("Invalid Input")


ff = FormFactory()  
l = ["Text","Password",'Email']
for inp in l:
    res = ff.create_form(inp)
    print(res)
'''


class Computer:
    # ram = None
    # rom =  None
    # graphics = None
    def __init__(self, ram, rom, graphics):
        self.ram = ram
        self.rom = rom
        self.graphics = graphics


    def get_configuration(self):
        print(f"""
        RAM:- {self.ram}
        ROM:- {self.rom}
        Graphics:- {self.graphics}
        """)


class Desktop(Computer):
    # ram = "8 GB"
    # rom =  "500 GB"
    # graphics = "2 GB"
    pass


class Laptop(Computer):
    # ram = "16 GB"
    # rom =  "1 TB"
    # graphics = "4 GB"
    pass


class ComputerFactory:
    def create_computer(self, comp_type,ram,rom,graphics):
        if comp_type in ['laptop', 'desktop']:
            resp = comp_type.title()
        else:
            raise ValueError(f"No any class present named :- {comp_type}")

        if resp:
            class_name = eval(resp)
            obj = class_name(ram,rom,graphics)
            return obj


cf = ComputerFactory()
obj_1 = cf.create_computer("laptop","4 GB","500 GB", "2 GB")
obj_2 = cf.create_computer("laptop","8 GB","1 TB", "4 GB")
obj_1.get_configuration()
obj_2.get_configuration()


