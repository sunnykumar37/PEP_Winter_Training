# Pattern for list comprehensions in Python
names = ['alice', 'bob', 'charlie', 'david', 'eve']
names2 = []
for name in names:
    if len(name) == 5:
        names2.append(name.title())
print(names2)


# dict comprehension
types = {'name': str, 'age': int, 'address': str}
new_names = {}
for t in types:
    new_names[t] = t.title()
print(new_names)