''' 
In the gregorian calender, three conditions are used to identify leap year:
The year cab be evenly divided by 4, is a leapmyear, unless:
The year can be evenly divided by 100, it is not a leap yearm unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the gregorian Calender, the year 2000 and 3400 are leap year,
1900, 2100, 2200, 2300, and 2500 are nit leap year'''

def is_leap(year):
    if(year % 4 ==0 and year % 100 != 0) or (year  % 400 == 0):
        return "Leap year"
    else:
        return "not a leap year"

year = int(input("Enter the year: "))
print(is_leap(year))
