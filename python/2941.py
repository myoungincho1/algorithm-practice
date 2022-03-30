S = input()

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro:
    if i in S:
        S = S.replace(i,'.')
print(len(S))