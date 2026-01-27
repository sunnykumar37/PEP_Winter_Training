a = ["Mannat", "Krishna", "surya"]
for i in range(len(a)):
    print(i,"-", a[i])

print("Using enumerate:")
for index, value in enumerate(a):
    print(index,"=", value)