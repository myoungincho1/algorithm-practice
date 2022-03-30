N = input()
ls = []
n =N
for i in range(len(n)):
    ls.append(int(n[-1]+n[:-1]))
    n = n[-1]+n[:-1]
print(sum(ls))