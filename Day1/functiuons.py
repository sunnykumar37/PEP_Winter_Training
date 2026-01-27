# 1. Function that takes arguments
def func1():
    print("This is a simple function.")
def add(a, b):
    return a + b

# 2. Function with default argument
def greet(name="User"):
    return f"Hello, {name}!"

# 3. Function with variable number of arguments
def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():   
    result = add(5, 3)
    print("Addition:", result)

    print(greet())
    print(greet("Sunny"))
    
    print("Sum:", total_sum(1, 2, 3, 4, 5))

if __name__ == "__main__":
    main()