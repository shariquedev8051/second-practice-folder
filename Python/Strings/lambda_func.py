# # Ananymous funtions are known as lambda functions


"""lambda argument_list:expression"""
# # * squar of numbers lambda function
# from functools import reduce
# def s(x): return x*x
# # print('Squar of a number:-',s(4))


"""sum of two numbers"""
# def s(a, b): return a+b
# # print("sum of numbers are",s(10,30))


"""finding the number is even or not"""
# l = [10, 23, 45, 56, 40, 111]
# # is_even = lambda num:True if num%2==0 else False
# l1 = list(filter(lambda x: x % 2 == 0, l))  # for even numbers
# # print(l1)
# l2 = list(filter(lambda x: x % 2 != 0, l))
# # print(l2) #for odd numbers
# # print("The number is even" if is_even(11) else "The number is odd")


"""Double the value of a list"""
# l1 = list(map(lambda x: x*2, l))
# # print(l1)


"""reduce function"""
# # l1 = reduce(lambda x,y:x+y,l)
# l1 = reduce(lambda x, y: x*y, l)
# # print(l1)
# def even_gen(num):
#     count = 2
#     for i in range(int(num)):
#         yield count
#         count += 2
# gen = even_gen(10)
# l = list(gen)
# print(l)

"""Difference Between map and lambda functions"""
# l = [x for x in range(10)]
# l1 = list(map(lambda x: x * 2, l))  # to manipulate the data
# l11 = list(map(lambda x: x + 2, l))  # to manipulate the data
# # To return the element when condition is true
# l2 = list(filter(lambda x: x % 2 == 0, l))
# # To return the element when condition is true
# l3 = list(filter(lambda x: x >= 5, l))
# l4 = list(filter(lambda x: x < 5, l))
# print(l1)
# print(l11)
# print(l2)
# print(l3)
# print(l4)
# l1 = ['zero', 'one', 'two', 'three', 'four',
#       'five', 'six', 'seven', 'eight', 'nine', 'ten']
# # var = dict(map(lambda x,y:{x:y},l1,range(0,10)))
# # print(var)
# l2 = range(11)
# print(tuple(zip(l1, l2)))
# # print(dict(zip(l2, l1)))


"""Sum of products"""
# from functools import reduce
# l = range(11)
# square = list(map(lambda x: x**2, l))
# SOP = reduce((lambda x,y:x+y),square)
# print(SOP)


"""Nested Lambda"""
# square = lambda x: x**2
# product = lambda f, n: lambda x: f(x) * 2
# print(product(square, 2)(20))


""""""



