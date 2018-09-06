import math

def lis_aux(arr):
	return lis_bf(arr,-math.inf,0)

def lis_bf(arr,prev,curr):
	if curr == len(arr):
		return 0
	taken = 0
	if arr[curr] > prev:
		taken = 1 + lis_bf(arr,arr[curr],curr+1)
	nontaken = lis_bf(arr,prev,curr+1)
	return max(taken,nontaken)

def lis_memo_aux(arr):
	d = [-1] * (len(arr)+1)
	for i in range(len(arr)):
		d[i] = [-1]*(len(arr))
	return lis_memo(arr,-1,0,d)

def lis_memo(arr,prev,curr,d):
	if curr == len(arr):
		return 0
	if d[prev+1][curr] >= 0:
		return d[prev+1][curr]
	taken = 0
	if prev < 0 or arr[curr] > arr[prev]:
		taken = 1 + lis_memo(arr,curr,curr+1,d)
	nontaken = lis_memo(arr,prev,curr+1,d)
	d[prev+1][curr] = max(taken,nontaken)
	return d[prev+1][curr]

def lis(arr):
    n = len(arr)

    lis = [1]*n

    prev = [0]*n
    for i in range(0, n):
        prev[i] = i

    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1:
                lis[i] = lis[j]+1
                prev[i] = j
    
    maximum = 0
    idx = 0

    for i in range(n):
        if maximum < lis[i]:
            maximum = lis[i]
            idx = i

    seq = [arr[idx]]
    while idx != prev[idx]:
        idx = prev[idx]
        seq.append(arr[idx])

    return (maximum, reversed(seq))

arr = [5,2,8,6,3,6,9,7]
ans = lis(arr)
print("Length of lis is", ans[0])
print("The longest sequence is", ", ".join(str(x) for x in ans[1]))

'''print(lis_aux([5,2,8,6,3,6,9,7]))
print(lis_memo_aux([5,2,8,6,3,6,9,7]))'''