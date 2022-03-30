N = int(input())
ls = list(map(int, input().split()))
s=0
for i in ls:
    if i == N:
        s += 1
print(s)