#picking and unpickling

import pickle


class Student:
    """Class to store the data related to student"""

    def __init__(self, name, roll_no) -> None:
        self.name = name
        self.roll_no = roll_no

    def __repr__(self) -> str:
        return f"{self.name} -- {self.roll_no}"


# s1 = Student("sharique", 334)
# s2 = Student("Sudhanshu", 335)
# s3 = Student("Ayush", 336)
# s4 = Student("Nargis", 337)
# list = [s1, s2, s3, s4]
# # for obj in list:
# #     print(obj)

# with open("stud.dat", 'wb') as f:
#     for obj in list:
#         pickle.dump(obj, f)

def load_data(fPath):
    with open(fPath, 'rb') as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break


objs = list(load_data("stud.dat"))
print(objs)
