ls =[]
for i in range(5):
    ls.append(input())

st = ''
while ls != ['','','','','']:
    for i in range(5):
        if ls[i] != '':
            st = st+ls[i][0]
        ls[i] = ls[i][1:]
