N = int(input())

six = ['0','1','2','3','4','5','6','7','8','9']
sex = '666'

lst = []

for a in six:
    for b in six:
        for c in six:
            for d in six:
                lst.append(int(sex+a+b+c+d))
for a in six:
    for b in six:
        for c in six:
            for d in six:
                lst.append(int(a+sex+b+c+d))
for a in six:
    for b in six:
        for c in six:
            for d in six:
                lst.append(int(a+b+sex+c+d))
for a in six:
    for b in six:
        for c in six:
            for d in six:
                lst.append(int(a+b+c+sex+d))
for a in six:
    for b in six:
        for c in six:
            for d in six:
                lst.append(int(a+b+c+d+sex))
sett = set(lst)
sett = sorted(sett)
print(sett[N-1])


# answer
N = int(input())

cnt = 0
six_n = 666
while True:
    if '666' in str(six_n):
        cnt += 1
    if cnt == N:
        print(six_n)
        break
    six_n += 1

