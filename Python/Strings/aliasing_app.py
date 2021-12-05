"""Aliasing means giving something same name for e.g (Rafeek bhai urf chota chatri)"""

# def hi(user):
#    return f"Hi {user}"

# hello = hi #here giving same name to a single functions
# print(id(hi))
# print(id(hello))
# print(hi("sharique"))
# print(hello('sharique'))


"""Function decorators"""
# without @decorator
# def decor(func):
#     def inner(name):
#         if name.lower() == 'sunny':
#             print("Bad morning sunny")
#         else:
#             func(name)
#     return inner
# @decor
# def wish(name):
#     print("Good morning "+name)
# decoreFunction = decor(wish) # closure or aliasing
# wish("sharique")
# wish("sunny")
# decoreFunction("sharique")
# decoreFunction("sunny")


# def decor(func):
#     def inner(num1,num2):
#         if num2 == 0:
#             return 'we can not devide by zero'
#         else:
#             return(func(num1,num2))
#     return inner

# @decor
# def divider(num1,num2):
#     return f"division is {num1/num2}"

# # devide_decore = decor(divider)

# # print(devide_decore(20,10))
# # print(devide_decore(20,0))
# print(divider(10,0))
# print(divider(10,20))

"""Chaining decorators"""


def decor(func):
    def inner():
        print('in decor function')
        func()
    return inner


def decor1(func):
    def inner():
        print('in decor1 function')
        func()
    return inner


@decor1
@decor
def msg():
    print("in function")


msg()
