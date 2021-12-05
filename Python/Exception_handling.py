# try:
#     num1 = int(input("Enter number1:- "))
#     num2 = int(input("Enter number2:- "))
#     print(num1 / num2)
# except ValueError as e:
#     print("Enter only integer values.")
# except ZeroDivisionError:
#     print("can not divide by zero")
# else:
#     print('Programm ran with any error')

# finally:
#     print('This will run even error occures')

class TooYoungeException(Exception):
    def __init__(self, arg):
        self.msg = arg


class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


age = int(input('Enter your age:- '))
if age <= 18:
    raise TooYoungeException("Come after sometime.")
elif age >= 50:
    raise TooOldException("ain't you too old for this things.")
else:
    print("Hurray You have so many apportunities")
