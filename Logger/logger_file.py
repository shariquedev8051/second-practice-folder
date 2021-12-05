# import logging

# logging.debug("Message from debug")
# logging.info("Message from info")
# logging.warning("Message from warning")
# logging.error("Message from error")
# logging.critical("Message from critical")

# LOGGER_FILE_PATH = r"D:\Python_playground\Practice\Logger\first_log.log"

# logging.basicConfig(format="%(asctime)s -- %(levelname)s -- %(message)s " ,filename=LOGGER_FILE_PATH, level=logging.DEBUG, datefmt='%d %B %Y %I:%M:%S')

# logging.debug("Message from debug")
# logging.info("Message from info")
# logging.warning("Message from warning")
# logging.error("Message from error")
# logging.critical("Message from critical")

# name = input("Enter your name :- ")

# try:
#     logging.info("Task started")
#     logging.debug(f"Entered by {name}")
#     inp1 = int(input("Enter first number:- "))
#     inp2 = int(input("Enter second number:- "))
#     logging.debug(f"First number {inp1}")
#     logging.debug(f"Second number {inp2}")
#     print(inp1/inp2)
#     logging.info('Task completed...!')
# except Exception as msg:
#     logging.error(msg, exc_info=False)


# import logging

# # create a custom logger
# testlogger =  logging.getLogger(__name__)
# logging.basicConfig(level='DEBUG') # To define basice level of debug
# testlogger.propagate = False # To stop logger to print twice

# #create handlers
# f_handler = logging.FileHandler('first_log.log')
# c_handler = logging.StreamHandler()
# f_handler.setLevel(logging.DEBUG)
# c_handler.setLevel(logging.WARNING)

# #create formatter and add to handler
# c_format = logging.Formatter("%(asctime)s -- [%(levelname)s] -- %(message)s")
# f_format = logging.Formatter('[%(levelname)s] -- %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)

# #Add handler to loggers
# testlogger.addHandler(c_handler)
# testlogger.addHandler(f_handler)


# testlogger.debug("Message from debug")
# testlogger.info("Message from info")
# testlogger.warning("Message from warning")
# testlogger.error("Message from error")
# testlogger.critical("Message from critical")


###practice
# import logging

# # Define test logger
# test_logger = logging.getLogger(__name__)
# logging.basicConfig(level="DEBUG")
# test_logger.propagate = False

# # Define file handlers and set their levels
# f_handler = logging.FileHandler("first_log.log")
# c_handler = logging.StreamHandler()
# f_handler.setLevel(logging.INFO)
# c_handler.setLevel(logging.ERROR)

# # Define formates for handler and add them to handler
# f_foramte = logging.Formatter("%(asctime)s -- [%(levelname)s] -- %(message)s", datefmt='%d %b %Y %I:%M:%S ')
# c_foramte = logging.Formatter("%(asctime)s -- [%(levelname)s -- %(message)s] ")
# f_handler.setFormatter(f_foramte)
# c_handler.setFormatter(c_foramte)

# # Add file handler to logger
# test_logger.addHandler(c_handler)
# test_logger.addHandler(f_handler)

# test_logger.debug("Msg from debug")
# test_logger.info("Msg from info")
# test_logger.warning("Msg from warning")
# test_logger.error("Msg from error")
# test_logger.critical("Msg from critical")

"""

LOGGER_FILE_PATH = r"D:\Python_playground\Practice\Logger\first_log.log" # absolute path
# LOGGER_FILE_PATH = r"first_log.log" # relative path

import logging
from logging.handlers import RotatingFileHandler

#define logger
test_logger = logging.getLogger(__name__)
logging.basicConfig(level="DEBUG")
test_logger.propagate=False

#defin file_handler
f_handler = RotatingFileHandler('log/MyLog', maxBytes=1000, backupCount=10)
f_handler.setLevel(logging.DEBUG)
 
#defin Format and add it to file_handler
f_formate = logging.Formatter("%(asctime)s -- %(levelname)s -- %(message)s")
f_handler.setFormatter(f_formate)

#Add file_handler to custom logger
test_logger.addHandler(f_handler)
f = open('file_name.txt','r') 
data = int(f.read())
for i in range(data ,data+10):
    test_logger.debug(f"Value of i is {i}")
    test_logger.debug("Msg from debug")
    test_logger.info("Msg from info")
    test_logger.warning("Msg from warning")
    test_logger.error("Msg from error")
    test_logger.critical("Msg from critical")
    test_logger.critical("-----------------------------")
data += 10
f.close()
f = open('file_name.txt','w') 
f.write(str(data))
f.close()
"""


'''
import logging
from logging.handlers import TimedRotatingFileHandler
import time

#define logger
test_logger = logging.getLogger(__name__)
logging.basicConfig(level="ERROR")
test_logger.propagate=False

#defin file_handler
f_handler = TimedRotatingFileHandler('log/MyLog', when = 's', backupCount=5)
f_handler.setLevel(logging.DEBUG)
 
#defin Format and add it to file_handler
f_formate = logging.Formatter("%(asctime)s -- %(levelname)s -- %(message)s")
f_handler.setFormatter(f_formate)

#Add file_handler to custom logger
test_logger.addHandler(f_handler)

a = time.time()

for i in range(20):
    test_logger.debug(f"Value of i is {i}")
    test_logger.debug("Msg from debug")
    test_logger.info("Msg from info")
    test_logger.warning("Msg from warning")
    test_logger.error("Msg from error")
    test_logger.critical("Msg from critical")
    test_logger.critical("-----------------------------")
    time.sleep(1)
b = time.time()

print(b-a)

'''