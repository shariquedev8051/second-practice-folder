"""without any class"""
# from threading import *


# def display():
#     for i in range(1, 11):
#         print("child thread")


# t = Thread(target=display)

# t.start()
# for i in range(1, 11):
#     print("Main Thread")

"""Creating multi threading using classes"""

# from threading import *
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("child thread-1")


# t = MyThread()
# t.start()

# for i in range(10):
#     print('Main thread-1')

"""Creating thread without using run()"""

# from threading import *

# class Test:
#     def display(self):
#         for i in range(10):
#             print("child class")

# obj = Test()
# t = Thread(target=obj.display)
# t.start()
# for i in range(10):
#     print("main class")

"""Counting active thread in the programm"""

# from threading import *
# import time
# def display():
#     print(current_thread().name, "...started")
#     time.sleep(3)
#     print(current_thread().name, "...Ended")


# t1 = Thread(target=display, name='Child Thread 1')
# t2 = Thread(target=display, name='Child Thread 2')
# t3 = Thread(target=display, name='Child Thread 3')
# t1.start()
# t2.start()
# t3.start()
# l = enumerate()
# for t in l:
#     print(t.name)
# print(f"Num of active thread are {active_count()}")
# time.sleep(5)
# print(f"Num of active thread are {active_count()}")
# l = enumerate()
# for t in l:
#     print(t.name)

item = []

def change_name():
    item.append(45)


print(item)
change_name()
print(item)