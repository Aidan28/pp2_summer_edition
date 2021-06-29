a = 1000
b = list(input().split())
for i in range(len(b)):
    s = int(b[i])
    if s < a and s > 0:
        a = s
print(a)
