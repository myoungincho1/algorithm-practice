N = int(input())
ls_x = []
ls_y = []

for i in range(N):
    x, y = list(map(int, input().split()))
    ls_x.append(x)
    ls_y.append(y)
rnk = [0 for i in range(N)]
tmp = 1
while 0 in rnk:
    idx_x = ls_x.index(max(ls_x))
    idx_y = ls_y.index(max(ls_y))
    if idx_x == idx_y:
        rnk[idx_x] = tmp
        tmp += 1
        ls_x[idx_x] = 0
        ls_y[idx_y] = 0
    else:
        idx_y_ls = []
        while True:
            idx_y_ls.append(idx_x)
            rnk[idx_x] = tmp
            ls_x[idx_x] = 0
            idx_x = ls_x.index(max(ls_x)) # new idx_x
            if idx_x == idx_y: 
                idx_y_ls.append(idx_x) 
                rnk[idx_x] = tmp
                tmp += len(idx_y_ls)
                for i in idx_y_ls:
                    ls_y[i] = 0
                    break
print(rnk)






