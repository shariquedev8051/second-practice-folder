"""Genrates Employee Data Randomly in list form"""

import random

class empDataGenrator:
    def __init__(self, id):
        self.ID = id
        

    def genEmpData(self, noOfEmployee): #id, name, age, salary, pin, city, state
        empList=[]
        city_state = {'Pune':'MH', 'Chennai': 'TamilNadu', 'Banglore':'Karnatka', 'Hydrabad': 'Telangana'}
        for i in range(noOfEmployee):
            cityName =  random.choice(list(city_state.keys()))
            list1 = [self.ID+i, empDataGenrator.empName(), random.randint(25,65), random.randint(15000,58000), random.randint(11111,99999), cityName, city_state.get(cityName)  ]
            empList.append(list1)
        return empList


    @staticmethod
    def empName():
        name =''
        for i in range(0, random.randint(4,6)):
            name += chr(65+random.randint(0,25))
        return name


def GenrateEmpData(id, number_of_employee):
    obj = "e"+f"{id}"
    obj = empDataGenrator(id)
    return obj.genEmpData(number_of_employee)

print(GenrateEmpData(100, 20))