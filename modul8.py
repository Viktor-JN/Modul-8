import datetime
import os
from time import sleep
from msvcrt import getwch

date = datetime.datetime.now()
print(date)
print(date.year)
print(date.strftime("%C"))
print(date.strftime("%y"))
print(date.strftime("%Y"))
print(date.strftime("%M"))
print(date.strftime("%H"))
print(date.strftime("%I"))
print(date.strftime("%p"))
x=0
while x<10:
    the_time = datetime.datetime.now()
    print(the_time.strftime("%H"))
    print(the_time.strftime("%M"))
    print(the_time.strftime("%S"))
    sleep(1)
    os.system("cls")
    x+=1
while True:
    print("Vill du starta ett tidtagarur (J)a (N)ej")
    answer=getwch().upper()
    if answer == "J":
        x=0
        while True:
            os.system('cls')
            print(x)
            sleep(1)
            x+=1
    elif answer == "N":
        break
    else:
        continue

