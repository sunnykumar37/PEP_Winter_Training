def swap(s):
    r = ''
    for c in s:
        if c.islower():
            r += c.upper()
        else:
            r += c.lower()

    return r
print(swap('Sun86ny'))
if __name__ == '__main__':
    swap('Sun86ny')