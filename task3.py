from urllib import request

s = str(request.urlopen("https://www.python.org/").read())
a = s[2: -1]
res = {}
for char in a:
    a.rstrip()
    c = a.count(char)
    res[char] = c
print(res)

with open('readme.md', 'r+') as f:
    for key, value in res.items():
        f.write(f"'{key}': ")
        f.write(f"{str(value)}\n")
