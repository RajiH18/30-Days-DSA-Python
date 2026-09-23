arr = [3, 5, 2, 8, 4]

prefix = []
total = 0

for i in arr:
    total = total + i
    prefix.append(total)

print(prefix)