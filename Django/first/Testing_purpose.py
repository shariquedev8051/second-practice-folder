# import random

# def bulk_create(self, number_of_employee):
#         city_list = ['Pune',
#                 'Nagpur',
#                 'Ajmer',
#                 'Delhi',
#                 'Kolkata',
#                 'Surat'
#                 ]
        
#         company_list = [
#             'Wipro',
#             'Infosys',
#             'Google',
#             'Yahoo'
#         ]
#      # @staticmethod        
#         def gen_name(min_length, max_length):
#             name = ""
#             for i in range(random.randint(min_length,max_length)):
#                 a = chr(random.randint(0,26)+65)
#                 name+= a
#             return name

#         # @staticmethod
#         def city(city_list):
#             return random.choice(city_list)

#         # @staticmethod
#         def gen_company(company_list):
#             return random.choice(company_list)

    

#         for e in range(number_of_employee):
#             print(f"name= {gen_name(4,6)} salary = {random.randint(35000,65000)} adr = {city(city_list)}company = {gen_company(company_list)}")
    
# bulk_create(100)


# def n_times(mul):
#     return lambda num : num*mul
# doubler = n_times(2)
# print(doubler(60))

for i in range(10):
    print(i)
