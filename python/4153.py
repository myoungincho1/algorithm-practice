while True:
    ls = list(map(int, input().split()))
    if ls == [0,0,0]:
        break
    max_num = max(ls)
    ls.remove(max_num)
    if max_num**2 == ls[0]**2 + ls[1]**2:
        print('right')
    else:
        print('wrong')