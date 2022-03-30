N, M = map(int, input().split())
ls = []
for i in range(N):
    ls.append(input())

wb = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
bw = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB',
'BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']

def numm(ls):
    count1 = 0
    count2 = 0
    for i in range(8):
        for j in range(8):
            if wb[i][j] != ls[i][j]:
                count1 += 1
    for i in range(8):
        for j in range(8):
            if bw[i][j] != ls[i][j]:
                count2 += 1
    return min(count1, count2)


ans = []
for i in range(N-7):
    for j in range(M-7):
        lst = []
        for k in range(8):
            lst.append(ls[i+k][j:j+8]) 
        ans.append(numm(lst))
print(min(ans))