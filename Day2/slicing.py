names = ["Sunny", "Arun", "Sahil", "Surya", "Mannat"]
print(enumerate(names))
print(list(enumerate(names)))

print(list((i - len(names), n)
    for i, n in enumerate(names)))

# Half-Open Interval
print(names[0:4])
print(names[:3])
print(names[2:])
print(names[-2:])
print(names[-4:-1])

names2 = names[:]  # Shallow Copy
print(id(names2))
print(id(names))

# Stride
print(names[::-1])
print(names[::2])
