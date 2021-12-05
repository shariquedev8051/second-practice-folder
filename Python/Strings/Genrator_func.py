"""Genrator function:- Which genrates the sequence when called"""

# """Genrate a even number genrator"""
# def even_gen(): #defining genrator
#     num = 0
#     while True:
#         if num<100:
#             num+=2
#             yield num
#         else:
#             yield "Limit is crossed"

# gen =even_gen()     #creating genrator object
# for i in range(1,60):
#     print(next(gen))    #executing the genrator




"""Prim number genrator"""

# def prim_num_gen():
#     prim_list = [2]
#     yield prim_list[-1]
#     num = 2
#     while True:
#         num+=1
#         for prim in prim_list:
#             if num%prim == 0:
#                 break
#         else:
#             prim_list.append(num)
#             yield num

                
# gen = prim_num_gen()
# for i in range(100):
#     print(f'{next(gen)} is a prime number.')




# """Fibonachi number genrator"""      
# def febonachi_gen():
#     f_list = [1,1]
#     while True:
#         yield f_list[-1]
#         num = f_list[-1]+f_list[-2]
#         f_list.append(num)

# gen = febonachi_gen()
# for i in range(10):
#     if i == 0:
#         print("[ ", end ='')
#     print(next(gen), end = " ")
# print("]")