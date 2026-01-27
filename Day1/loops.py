def main():
    # 1. define a while loop
    i = 1
    while i <= 3:
        print("While loop:", i)
        i += 1


    # 2. define a for loop
    for j in range(1, 4):
        print("For loop:", j)


    # 3. use a for loop over a collection
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print("Fruit:", fruit)


    # 4. use break and continue
    for num in range(1, 6):
        if num == 3:
            continue
        if num == 5:
            break 
        print("Number:", num)


    # 5. using enumerate to get index
    for index, fruit in enumerate(fruits):
        print("Index:", index, "Value:", fruit)


if __name__ == "__main__":
    main()
