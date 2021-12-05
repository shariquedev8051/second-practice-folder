"""Genrates Employee Data Randomly in Dictonary Form"""

import random

class empDataGenrator:
    def __init__(self, id):
        self.ID = id
        

    def genEmpData(self, noOfEmployee): #id, name, age, salary, pin, city, state
        empdict={}
        city_state = {'Pune':'MH', 'Chennai': 'TamilNadu', 'Banglore':'Karnatka', 'Hydrabad': 'Telangana'}
        for i in range(noOfEmployee):
            cityName =  random.choice(list(city_state.keys()))
            empdict[self.ID+i] = {
                "Id":self.ID+i,
                "Name": empDataGenrator.empName(),
                'Age': random.randint(25,65),
                "Salary": random.randint(15000,58000),
                 "Addr": {
                    "PIN"  :random.randint(11111,99999),
                    'City': cityName,
                    'State': city_state.get(cityName)  
                }
                }
            # empList.append(list1)
        return empdict


    @staticmethod
    def empName():
        name =''
        for i in range(0, random.randint(4,6)):
            name += chr(65+random.randint(0,25))
        return name


def GenrateEmpData(id, number_of_employee):
    obj = empDataGenrator(id)
    return obj.genEmpData(number_of_employee)

for id, data in GenrateEmpData(100, 20).items():
    print(f"Id: {id}-------",f'Data: {data}')
