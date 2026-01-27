# can loop over lists,  strngs, iterators, dicts... sequesnce-like objects
students = {"Name": ["Sunny", "Arun", "Sahil", "Surya", "Krishna"], "Roll_no": [13, 22, 3, 44, 5]}
for keys in students.keys():
    print(keys)
for values in students.values():
    print(values)
n  = "Sunny"
print(n.upper())
print(n.title())
print(n.find("n"))
print(n.replace("n", "N"))
print(n[-1])