N = int(input())

def pi(n):
    if n==0 :
        return 0
    elif n==1 or n==2:
        return 1
    return pi(n-1) + pi(n-2)
print(pi(N))