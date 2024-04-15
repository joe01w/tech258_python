# Python Standard Library

# The standard library consists of many modules and packages
# that are very useful,
# and so were added to python by default.

import random
import math
import os
import sys
import datetime
import builtins
import requests
# can import all of them like: import random, math, os, etc

# random demo
print(random.random())
print(random.randrange(1, 11))

# math demo
num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
print(f"remainder from 1/5: {math.remainder(1, 5)}")

# os demo

# returning current working directory
working_dir = os.getcwd()
print(f"Current working directory is: {working_dir}")

# get user
username = os.environ.get("USERNAME") or os.environ.get("USER")
print(f"Username is: {username}")

#cpu cores
cpu_cores = os.cpu_count()
print(f"Amount of CPU cores: {cpu_cores}")

# make directory
# os.mkdir("test_dir")


# sys demo

print(f"Current path: {sys.path}")
print(sys.version)

# datetime demo

print(f"Today's date is: {datetime.datetime.today()}")

# builtins demo

# This shows all the built-in python packages.
# for name in dir(builtins):
#     if name[0].islower():
#         print(name)

# requests demo

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code) # 200 --> Okay
print(request_bbc.content) # print out the raw html of the bbc website

