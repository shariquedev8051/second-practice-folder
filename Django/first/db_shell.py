
import random
from datetime import date
from app1.models import *

#!! exec(open("D:\\Vscode_Project\\Django_b5\\first\\db_shell.py").read())
# * methode 1:
# e = Employee (name='Shark', salary=200000, address='nagpur')
# e.save()
# object -- model manager

# * methode 2:
# Employee.objects.create(name='aaa', salary=225000, address='wardha')

# * To read data *

# all -- +ve indexing[], first have __dict__
# all_data = Employee.objects.all()
# all_data = Employee.objects.first().__dict__
# all_data = Employee.objects.all()# *need to convert it to list as employee object type
# * is django so we need convet it into list
# print(all_data)

# * to get query set
# print(all_data.query)

# SELECT "app1_employee"."id", "app1_employee"."name", "app1_employee"."salary", "app1_employee"."address" FROM "app1_employee"
# emp = Employee.objects.filter(name = "Xyz")
# print(emp.query)


# * creating employees
# import random
# add_list = ["Pune",'Hydrabaad','chennai','Nagpur']
# for i in range(0, 26):
#     Employee.objects.create(name = chr(65+i), salary = random.randint(35000, 85000), adr = random.choice(add_list))

# formate1 = """--------ID:- {}---------
# Name:- {}
# Salary:- {}
# Address:- {}
# """
# for i in Employee.objects.all():
#     print(formate1.format(i.id,i.name, i.salary, i.adr))


# * practice
# emp =Employee.objects.all()
# emp = Employee.objects.get(id = 9) # ! if it return more than one employee it will pass error for e.g name = "A" having same names
# emp = Employee.objects.filter(name = 'A' ).count() # return queryset
# emp = Employee.objects.filter(name = 'A' ) #* return queryset
# print(emp[0].name)
# print(emp[0].salary)
# print(emp[0].address)
# print(emp)


# * To exclude the a record
# emp = Employee.objects.all().exclude(name = 'A').count()
# print(emp)


# * To print data
# formate1 = """--------ID:- {}---------
# Name:- {}
# Salary:- {}
# Address:- {}
# """
# for i in Employee.objects.all():
#     print(formate1.format(i.id,i.name, i.salary, i.adr))


# * To convert data into list
# def get_employee_dict():
#     emp_list = []
#     for i in Employee.objects.all():
#         emp_list.append({'ID':i.id, 'Name': i.name, 'Salary':i.salary, 'Address':i.address})
#     return emp_list
# print(get_employee_dict())


# * lambda
# total_payout = 0
# for i in Employee.objects.all():
#     total_payout += i.salary
# print(total_payout)


# * Avg value
# from django.db.models import Avg
# emps = Employee.objects.all().aggregate(Avg('salary'))
# emps = Employee.objects.all().aggregate(Max('salary'))
# print(emps)


# * Update employee data fetching with id
# def update_emp(id, name):
#     try:
#         emp = Employee.objects.get(id = id)
#     except Employee.DoesNotExist as msg:
#         print(f'No employee found with the ID: {id}\n{msg}')
#     else:
#         emp.name = name
#         emp.save()
# update_emp(int(input('Enter id of employee:- ')), 'ABC')


# * incrementing salary by 5% if greater than 50000
# def increment_salary(inc_per):
#     emp = Employee.objects.all()
#     for e in emp:
#         if e.salary >= 50000:
#             e.salary += e.salary*(inc_per/100)
#             print(f'Salary increased for {e.name} and ID is {e.id}')
#             e.save()
# increment_salary(50)


# * updating all column
# emp = Employee.objects.all().update(company = 'TCS')


# * updating filtered
# emp = Employee.objects.filter(id = 20).update(company = 'Google')


# * Checkjing attributes
# print(hasattr(Employee.objects.all(), 'update'))


# * greater than and equal to
# emps = Employee.objects.filter(id__gte = 5)
# emps = Employee.objects.filter(id__gt = 5)
# emps = Employee.objects.filter(id__gte = 5).count()
# emp = Employee.objects.filter(id__lte = 5)
# emp = Employee.objects.filter(id__lt = 5)
# emp = Employee.objects.filter(id__lte = 5).count()
# print(emp)


# * Name startswith and ends with
# emps = Employee.objects.filter(name__startswith = 'a').count()
# emps = Employee.objects.filter(name__iendswith = 'a') # also capital results too
# emps = Employee.objects.filter(name__endswith = "e").count()
# emps = Employee.objects.filter(name__eendswith = "e").count()#includes results with capital too
# print(emps)


# * To delete one employee
# def delete_emp_by_id(eid):
#     emp = Employee.objects.get(id=eid)
#     emp.delete()
# delete_emp_by_id(22)


# * To delete all data
# Employee.objects.all().delete()


# * Genrat Licence data
# from datetime import date

# emp = Employee.objects.get(id = 23)
# l = Licence(licence_no = "LXCV123456789", expiry_data=date(2035, 12, 11), dl_type="MCWG", employee=emp)
# l = Licence(licence_no = "LXCV123456785", expiry_data=date(2035, 12, 11), dl_type="MCWG", employee_id=25)
# l.save()

# * to get licence number from employee id

# emp = Employee.objects.get(id = 25)
# l = Licence.objects.get(employee_id = emp.id)

# emp = Employee.objects.get(id =24)
# print(emp.licence.licence_no)

# l= Licence.objects.get(licence_no = 'LXCV123456785').expiry_date

# emp = (Employee.objects.get(id =25)).name
# print(emp)

# l= Licence.objects.get(licence_no = 'LXCV123456785').employee #* Better option
# print(l.name)


# object create
# update
# delete
# read

# * saving name using licence object
# l = Licence.objects.get(licence_no = 'LXCV123456785').employee
# l.name = 'Rohan'
# l.save()

# * fectching license of an employee usning employee_name
# print(Licence.objects.get(employee__name = 'Rohan'))

# * fectching license of an employee usning employee_id
# print(Licence.objects.get(employee__id = 25))

# * directely passing employee object
# print(Licence.objects.get(employee=24))

# * to delet an employee having a licence number delet licence first then employee
# l = Licence.objects.get(licence_no= 'LXCV123456789')
# print(l.get_employee())

# * changing employee object
# l.change_employee_address('Nagpur')

# * get licence object
# print(Licence.get_licence_object('LXCV123456789'))

# Employee.objects.all().delete()

def bulk_create(number_of_employee):
    city_list = ['Pune',
                 'Nagpur',
                 'Ajmer',
                 'Delhi',
                 'Kolkata',
                 'Surat'
                 ]

    company_list = [
        'Wipro',
        'Infosys',
        'Google',
        'Yahoo'
    ]
    # @staticmethod

    def gen_name(min_length, max_length):
        name = ""
        for i in range(random.randint(min_length, max_length)):
            a = chr(random.randint(0, 26)+65)
            name += a
        return name

    # @staticmethod
    def city(city_list):
        return random.choice(city_list)

    # @staticmethod
    def gen_company(company_list):
        return random.choice(company_list)

    for e in range(number_of_employee):
        Employee.objects.create(name=gen_name(4, 6), salary=random.randint(
            35000, 65000), adr=city(city_list), company=gen_company(company_list))

# bulk_create(100)
# emp = Employee.objects.get(id =24)
# Task.objects.create(name = "Create login page" ,timeline = str(date(2021,8,12)), employee =emp)
# Task.objects.create(name='Create email fuctionality')
# Task.objects.create(name='create landing page')


def assign_task(emp_id, timeline, task_id):
    emp = Employee.objects.get(id=emp_id)
    t1 = Task.objects.get(task_id=task_id)
    t1.employee_id = emp
    t1.timeline = str(timeline)
    t1.save()


# assign_task(27, date(2021,8,16),1)
# emp = Employee.objects.get(id=27)
# print(emp.task_set.all()) #* for one to many -- data fetch
# print(len(emp.task_set.all()))#* To count the number of task assigned to an employee

# t = Task.objects.get(task_id = 1)
# print(t.employee)#* to read employee using task_object

# emp = Employee.objects.get(id=27)
# print(emp.get_task_count()) #* using Employee methode

# t = Task.objects.get(task_id =1)
# print(t.get_employee())

# emp = Employee.objects.get(id = 27)
# print(emp.tasks.all()) #* Using related name replacing task_set

###############################################################


# hawaiian_pizza = Pizza.objects.create(name = 'Hawaiian')
# pineapple = Topping(name='pineapple')
# pineapple.save()
# hawaiian_pizza.toppings.add(pineapple)
# pizza = Pizza.objects.get(id =3 )
# t1 = Topping(name= 'Capsicum')
# t1.save()
# pizza.toppings.add(t1)

# print(pizza.toppings.all())
# pizza1 = Pizza.objects.create(name = 'Cheese')
# t1 = Topping.objects.get(id =3)
# t2 = Topping.objects.get(id= 4)
# pizza1.toppings.add(t1)
# pizza1.toppings.add(t2)

# t1 = Topping.objects.get(id= 3)
# print(t1.pizza_set.all())
# print(t1.pizzas.all())
# Employee.objects.all().delete()


# * Creating pizz and toppings objects
# p1 = Pizza.objects.create(name = 'Hawaiian')
# p2 = Pizza.objects.create(name='Cheese')
# t1 = Topping.objects.create(name='Pineapple')
# t2 = Topping.objects.create(name='Capsicum')
# p1 = Pizza.objects.get(id=1)
# p2 = Pizza.objects.get(id=2)
# t1 = Topping.objects.get(id=1)
# t2 = Topping.objects.get(id=2)


# * Adding toppings to the pizza
# p1.toppings.add(t1)
# p1.toppings.add(t2)
# p2.toppings.add(t1)
# p2.toppings.add(t2)


# * Accessing topping using pizza object
# p1 = Pizza.objects.get(id=1)
# t=p1.toppings.all()
# print(t)
# print(Pizza.objects.get(id=1).toppings.all()) #* in one line


# * For accessing pizza using topping
# t1 = Topping.objects.get(name = "pineapple")
# print(t1.pizza_set.all()) #* If related name is not defined
# print(t1.pizzas.all())


#* fetching pizza with topping starting name
# print(Pizza.objects.filter(toppings__name__istartswith="p"))#* istartwith for case incensitive


#* Fetching pizz through toppings
# print(Topping.objects.filter(pizzas__name__contains = 'Hawaiian'))

