import random

from django.db import models
from django.db.models.deletion import CASCADE


class Common_class(models.Model):

    def __str__(self):
        if type(self) == Employee:
            return f"{self.id}--{self.name}"
        elif type(self) == Licence:
            return f"{self.licence_no}--{self.expiry_date}"
        elif type(self) == Task:
            # return f'{self.task_id} -- {self.name}'
            return f'{self.__dict__}'
        elif type(self)== Project:
            return f'{self.project_id} -- {self.name}'
    def __repr__(self):
        return str(self)

    class Meta:
        abstract = True


class Employee(Common_class):  # id is automatically defined # app1_employee
    # ! Still they look like class variable
    name = models.CharField(max_length=100)
    salary = models.FloatField()  # ! but are instant variable
    adr = models.CharField(max_length=500)
    company = models.CharField(max_length=100, default='infosys')

    class Meta:  # ! Meta should be capital
        db_table = 'emp'

    def get_name_with_salary(self):
        return f'Name: {self.name} Salary:{self.salary}'
    
    def get_task_count(self):
        return len(self.task_set.all())


class Licence(Common_class):
    # ? Autofield will remove default id as primary key
    licence_no = models.CharField(primary_key=True, max_length=20)
    expiry_date = models.DateField()
    dl_type = models.CharField(max_length=10)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Licence'

    def get_employee(self):
        return self.employee

    def change_employee_address(self, nadr):
        self.employee.adr = nadr
        # self.employee.save() #? First methode
        # Employee.save()        #? Second methode

    @staticmethod
    def get_licence_object(Glicence_no):
        return Licence.objects.get(licence_no=Glicence_no)


class Task(Common_class):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    timeline = models.DateTimeField(null=True)
    task_created_date = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, related_name='tasks')

    class Meta:
        db_table = "task"


    def get_employee(self):
        return self.employee


class Project(Common_class):
    project_id = models.AutoField(primary_key=True, )
    description = models.TextField(null=True)
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=15)
    client = models.CharField(max_length=16)
    employee = models.ManyToManyField(Employee, db_table='emp_project')

    class Meta:
        db_table = 'project'

    




###############################

class CommonPizza(models.Model):
    
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Topping(CommonPizza):
    # pizzas = models.ManyToManyField('Pizza')
    pass

class Pizza(CommonPizza):
    toppings = models.ManyToManyField('Topping', related_name='pizzas') 

    #! if we are accessing toppping from pizza ie. pizza.toppings.add(t1)
    #! it get trickire when we go from top to bottom ie from topping to pizza
    #! which t1.pizza_set.all()
    #? if we give related name than it becomes 
    #? t1.pizzas.all()