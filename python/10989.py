import sys
N = int(input())
input_list = []
for _ in range(N):
    input_list.append(int(sys.stdin.readline()))

def counting_sort(array, max):
    counting_array = [0]*(max+1)

    for i in array:
        counting_array[i] += 1
    
    for j in range(1, max):
        counting_array[j] += counting_array[j-1]
    
    output_array = [-1]*len(array)

    for i in array:
        output_array[counting_array[i] - 1] = i
        counting_array[i] -= 1
    return output_array
output = counting_sort(input_list, max(input_list))
for i in range(N):
    print(output[i])



#solution
import sys
N = int(sys.stdin.readline())

check_list = [0]*10001
for _ in range(N):
    check_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)













