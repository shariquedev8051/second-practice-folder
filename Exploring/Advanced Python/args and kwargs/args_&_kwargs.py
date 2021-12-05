def student(name , age , roll_no):
    print(f"The name of student is {name}, age is {age} and roll number is {roll_no}.")

def student_args(*args) :# type is tupple of *args also name doesn't matter * does
    print(type(args))
    print(f"The name of student is {args[0]}, age is {args[1]} and roll number is {args[2]}.")


def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)


lis = [1,2,3,4]
dict = {
    "name":"Hi",
    "2": "Hello",
    "3" : "Tata" 
    }
# student("Sharique", 31, 44)
# student_args("Sharique", 31, 44)

master("Bolo",*lis,**dict)

# print(dict["name"])

