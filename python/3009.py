ls_x = []
ls_y = []
result = []
for i in range(3):
    x, y = map(int, input().split())
    ls_x.append(x)
    ls_y.append(y)

if ls_x.count(min(ls_x)) == 1:
    result.append(min(ls_x))
else:
    result.append(max(ls_x))
if ls_y.count(min(ls_y)) == 1:
    result.append(min(ls_y))
else:
    result.append(max(ls_y))
print(result[0],result[1])

