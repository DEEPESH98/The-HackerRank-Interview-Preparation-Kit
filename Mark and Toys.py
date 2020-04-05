a, k = input().split()


price_list = list(map(int, input().rstrip().rsplit()))

price_list.sort()
sum = 0
count = 0
for i in range(0, len(price_list)):
    if sum < int(k) or sum == int(k):
        sum = sum + price_list[i]
        count = count + 1

print(count - 1)
