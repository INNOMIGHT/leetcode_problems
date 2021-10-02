R,C=[],[]   
m=int(input())
n=int(input())
arr=[]
for i in range(m):
    arr.append(list(map(int,input().split())))
#finding sum of each row
for i in range(m):
    sum=0
    for j in range(n):
        sum += arr[i][j]
    R.append(sum)
#finding sum of each column
for i in range(m) :
    sum=0
    for j in range(n) :
        sum += arr[j][i]
        C.append(sum)
print(max(R)+max(C))

