date = input("Enter date: ")
time = input("Enter time: ")

name = "Sunny"

if date.lower() == "1 jan":
    wish = f" Happy New Year! Today's date is {date} at {time}."
elif date.lower() == "13 feb":
    wish = f" Happy Birthday! Today's date is {date} at {time}."
else:
    wish = f"Hope you have a wonderful day! Today's date is {date} at {time}."

p = f"""
Greetings! {name.title()},

{wish}

Warm regards
"""
print(p)

from datetime import datetime

date_input = input("Enter date (DD Mon, e.g. 01 Jan): ")
time = input("Enter time: ")
name = "Sunny"

try:
    date_obj = datetime.strptime(date_input, "%d %b")

    if date_input.lower() == "01 jan":
        wish = "Happy New Year!"
    elif date_input.lower() == "13 feb":
        wish = "Happy Birthday!"
    else:
        wish = "Hope you have a wonderful day!"

    p = f"""
Greetings! {name.title()},

{wish} Today's date is {date_input} at {time}.

Warm regards
"""
    print(p)

except ValueError:
    print("❌ Invalid date! Please enter in format: DD Mon (e.g. 01 Jan)")
