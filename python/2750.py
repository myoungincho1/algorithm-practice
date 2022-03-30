N = int(input())
ls = []
for i in range(N):
    ls.append(int(input()))
ls = sorted(ls)
for j in range(N):
    print(ls[j])