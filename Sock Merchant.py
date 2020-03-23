c=int(input())
a = list(map(int, input().rstrip().split()))
b = list(set(a))
new_list = []
final = 0

for i in range(0,len(b)):
    com = 0
    value = b[i]
    for j in range(0,len(a)):
        if value==a[j]:
            com = com + 1
    new_list.append(com)

for i in range(0,len(new_list)):
    temp = int(new_list[i]/2)
    final = final + temp

print(final)
