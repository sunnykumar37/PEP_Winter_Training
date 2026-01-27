def Series():
    a  = 0
    b  = 1
    p = 0
    n = int(input("Enter the number of terms: "))
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=' ')
        p = a + b
        a = b
        b = p

Series()