def split_join():
    #s = input("Enter a input: ")
    s = ("Hello World " \
         "This is Python")
    p = s.split()
    print(p)
    r = "-".join(p)
    print(r)
if __name__ == "__main__":
    split_join()