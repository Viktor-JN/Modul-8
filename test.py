import datetime

x = int(input("""Skriv in ett år, månad och dag och se hur lång tid det är tills dess
Börja med år, sen månad och sist dag\n"""))
y = int(input())
z = int(input())

compare_date = datetime.datetime(x, y, z)

print(compare_date.strftime("%Y"), compare_date.strftime("%m"), compare_date.strftime("%d"))

today = datetime.datetime.now()

year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")

compare_year = (int(year)-x)*365
compare_month = (int(month)-y)*30
compare_day = int(day)-z
total=compare_day+compare_month+compare_year
print(f"Det är {total} dagars skillnad")