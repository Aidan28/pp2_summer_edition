a = int(input())
dictionary = {}
for i in range(a):
    key, value = input().split()
    dictionary[key] = value
    dictionary[value] = key
print(dictionary[input()])