string = str(input())

string = string.lower()

glasnie = ['a', 'o', 'i', 'e', 'y', 'u']

a=''

for i in glasnie:
    string = string.replace(i, '')


for i in string:
    a += f'.{i}'

print(a)
