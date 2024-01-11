a = []
for i in range(3):
    a = a + [int(input())]
a.sort()
max = a[2]
min = a[0]
print(max,min)

print(a)