N = int(input())

res = 1
temp = 1
while True:
    if N <= temp:
        break
    else:
        temp += 6*res
        res += 1
print(res)

