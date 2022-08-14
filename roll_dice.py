import random
from tokenize import Number
def rolldice(min,max):
    while True:
        print("rolling a dice...")
        print(f"your number:{random.randint(min,max)}")
        choice = input("do you want to roll a dice again?(y/n")
        if choice.lower() == 'n':
            break

   


    
