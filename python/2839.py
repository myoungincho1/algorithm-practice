N = int(input())
lst = []
for i in range(N//5+1):
    n = N-5*i
    if n%3==0:
        lst.append(i + n//3)
if lst == []:
    print(-1)
else:
    print(min(lst))