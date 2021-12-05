
# class Employee:
#     """This is an employee class"""
#     COMPANY = "infosys"

#     def __init__(self, name="Sharique", age=31, adr="Amravati", sal=35000):
#         self.name = name
#         self.age = age
#         self.adr = adr
#         self.salary = sal


"""
# How to add data to the class?
# By adding all keyword arguments
e1 = Employee("Neha",34,"Pune")
# print(e1.__dict__)
e2 = Employee()


#How to add new instance variable
e1.salary = 35000
# print(e1.__dict__)

# How to add a static variable
Employee.CEO = "Bil Gates"  # Once you add static variable using class name It will be available for each and object.Even for the objects was created after.

# How to get values of instance variable 
# print(e1.adr)
# print(e1.company)
e1.COMPANY = "Wipro"
print(e1.COMPANY)
del e1.COMPANY
print(e1.COMPANY)
# How to add 
"""

"""
class test:
    def add_sallary(emp):
        emp.salary += 10000


e1 = Employee()
print(e1.salary)
test.add_sallary(e1)
print(e1.salary)

"""

# First methode genrating a class object inside a class method


# class Employee:
#     """This is an employee class"""
#     COMPANY = "infosys"

#     def __init__(self, name, age, adr, sal):
#         self.name = "Sharique"
#         self.age = 31
#         self.adr = "Amravati"
#         self.salary = 35000
#         # Get the object of car and storing it in instance varible
#         self.car = Car("Innova", "2.5V", 'Grey')

#     def get_emp_info(self):
#         print(f"""
#             Name :- {self.name}
#             Age :- {self.age}
#             Address :- {self.adr}
#             salary :- {self.salary}
#         """)
#         self.car.get_car_info()  # Here self.car is an instance varibale refernce of car object


# class Car:
#     """Car which is owen by employees"""

#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def get_car_info(self):
#         print(f"""
#             Car Name:-{self.name}
#             Model number:{self.model}
#             Color is {self.color}
#             """)


# # c = Car("Innova", "2.5V", 'Grey')
# e = Employee("Sharique", 32, 'Amravati', 90000)
# e.get_emp_info()


# methode 2 Passing the external variable value in a class
# class Employee:
#     """This is an employee class"""
#     COMPANY = "infosys"

#     def __init__(self, name, age, adr, sal, car):
#         self.name = "Sharique"
#         self.age = 31
#         self.adr = "Amravati"
#         self.salary = 35000
#         self.car = car  # Get the object of car and storing it in instance varible

#     def get_emp_info(self):
#         print(f"""
#             Name :- {self.name}
#             Age :- {self.age}
#             Address :- {self.adr}
#             salary :- {self.salary}
#         """)
#         self.car.get_car_info()  # Here self.car is an instance varibale refernce of car object


# class Car:
#     """Car which is owen by employees"""
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color
#     def get_car_info(self):
#         print(
#             f'Car Name:{self.name}, model number:{self.model} and color is {self.color}')


# c = Car("Innova", "2.5V", 'Grey')
# e = Employee("Sharique", 32, 'Amravati', 90000, c)
# e.get_emp_info()
# class Student:
#     collegeName = "P.R.PCE"
#     def __init__(self,name):
#         self.name = name

# print(Student.collegeName)
# s = Student("Sharique")
# print(s.name)


# class P:
#     def property(self):
#         print("Gold, cas and money.")
#     def marry(self):
#         print("sultana")


# class C(P):
#     def marry(self):
#         super().marry()
#         print("Katrina Kaif")

# c = C()
# c.property()
# c.marry()

# class p:
#     def __init__(self):
#         print('In parent constructor')


# class C(p):
#     def __init__(self):
#         print('in child constructor')

# c = C()

"""Inheritance"""
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, roll_no, major):
#         super().__init__(name, age)
#         self.roll_number = roll_no
#         self.major = major

#     def student_info(self):
#         print(f"""
#         Name :- {self.name}
#         Age :- {self.age}
#         Roll No:- {self.roll_number}
#         Major :- {self.major}
#         """)


# s = Student('Sharique', 31, 4366, "electronics")
# s.student_info()

"""Operator Overloading"""
# class Book:
#     def __init__(self,pages):
#         self.pages = pages

#     def __add__(self,other):
#         return self.pages + other.pages

# b1 = Book(100)
# b2 = Book(100)
# print(f'Total number of pages are {b1+b2}')

"""public, private and protected"""
# class A:
#     x = 10
#     _y = 20
#     __z = 30

#     def display(self):
#         print(self.x)
#         print(self._y)
#         print(self.__z)
#         print('___________________')

# class B(A):
#     def display_b(self):
#         print(self.x)
#         print(self._y)
#         print(self._A__z)  # _className__varibalName to access protected varible
#         print('___________________')

# a = A()
# b = B()
# a.display()
# b.display_b()
# print(a.x)
# print(a._y)
# print(a._A__z)
