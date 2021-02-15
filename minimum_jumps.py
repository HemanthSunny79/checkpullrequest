arr = [1, 3, 6, 1, 0, 9]
#O(n^2) approach cloud jumping
jumps=[float('inf') for i in range(len(arr))]
jumps[0]=0
n= len(arr)
for i in range(1,n):
    print(i,end=" ")
    for j in range(i):
        if(i<=arr[j]+j and jumps[j]!= float('inf')):
            jumps[i]=min(jumps[i],jumps[j]+1)
            print("----",jumps[i],j)
            break

print(jumps)

#O(n) approach
#Beautiful approach refer gfg
#https://www.geeksforgeeks.org/minimum-number-jumps-reach-endset-2on-solution/
print("-------------------------\n")
n=len(arr)
if(n==1):
    print(0)
    exit()
if(n<=0):
    print(-1)
    exit()
max_reach=arr[0]
steps=arr[0]
jump=1
for i in range(1,n):
    if(i==n-1):
        print(jump)
        break
    max_reach=max(max_reach,i+arr[i])
    steps-=1
    if(steps==0):
        jump+=1
        if(i>=max_reach):
            print(-1)
            break
        steps=max_reach-i

    
        




