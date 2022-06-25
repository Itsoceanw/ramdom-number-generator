#ramdom number generator make by Itsoceanw
import random
number = random.randint(0,999)
print(number)
restart = input("Run again? (y/n) ")
if restart == "y":
    print(number)
else: 
    print("ok bye :)")
    exit()
