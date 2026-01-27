# creating the virtual environment for the project 
# 1. python -m venv venv
# 2. source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)

print("Hello World")


def main():
    x, y = 5, 10
    if x > y:
        print(f"{x} is greater than {y}")
    elif y > x:
        print(f"{y} is greater than {x}")
    else:
        print("Both numbers are equal")
if __name__ == "__main__":
    main()