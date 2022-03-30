N = int(input())
ls = []
for _ in range(N):
    ls.append(int(input()))
ls.sort()
for j in range(N):
    print(ls[j])