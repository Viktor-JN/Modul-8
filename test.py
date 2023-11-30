import datetime
from datetime import date
import msvcrt
from os import system
while True:
    system('cls')
    x = int(input("""Skriv in ett år, månad och dag och se hur lång tid det är tills dess
Börja med år, sen månad och sist dag\n"""))
    y = int(input())
    z = int(input())

    compare_date = date(x, y, z)
    while True:
        print(compare_date)
        print("Är det korrekt (J)a eller (N)ej")
        answer = msvcrt.getwch()
        if answer.upper() == "J":
            break
        elif answer.answer() == "N":
            break
        else:
            continue
    if answer.upper() == "J":
        break
    elif answer.upper() == "N":
        continue

today = date.today()
delta_date = compare_date-today
if delta_date > 0:
    print(f"Det är {delta_date} dagars skillnad från idag")
else: 
    print(f"")