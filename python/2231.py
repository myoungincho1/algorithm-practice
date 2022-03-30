N = int(input())

def gen(n):
    ls = []
    for i in range(1,n+1):
        if i + sum(list(map(int,list(str(i))))) == n:
            ls.append(i)
    if ls == []:
        return 0
    else:
        return min(ls)
print(gen(N))