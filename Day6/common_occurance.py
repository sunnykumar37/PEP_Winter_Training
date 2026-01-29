''' 
Given a string, which is the company name in lowercase letters, your task is to find the
top three most common characters in the string.
Print the three most common characters along with their occurrence counts.
sort the descending order of occurrence count.
if the occurrence count is the same, sort the characters in alphabetical order.
'''
s = input().strip()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
chars = list(freq.keys())

chars.sort(key=lambda x: freq[x], reverse=True)
for ch in chars[:3]:
    print(ch, freq[ch])
