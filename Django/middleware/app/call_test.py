
class Student:
    def __init__(self, name):
        self.Name = name

    # def __repr__(self): # Return when want to print object of class
    #     return f"name is {self.Name}"
    
    def __call__(self, marks): # make objects callable
        print(f"marks are {marks}")

s1 = Student("Piyush")
s1(65)