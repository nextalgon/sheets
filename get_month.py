import time
from datetime import datetime


def get_time():
    myobj = datetime.now()
    return myobj


while True:
    a = input()
    if a:
        print(get_time())