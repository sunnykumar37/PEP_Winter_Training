# num = 10
# assert num> 10

try:
    num = int(input("Enter the even number: "))
    assert num%2 == 0
    print("The number is even")
except AssertionError:
    print("Please enter even number")