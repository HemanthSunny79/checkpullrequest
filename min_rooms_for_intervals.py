#https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
arr = [1,2,3,4,5,6,7,7,8]
dep = [2,6,9,5,7,6,10,12,9]
arr.sort()
dep.sort()
rooms_req=0
i=0
j=0
n=len(arr)
ans=float('-inf')
while(i<n and j<n):
    print(rooms_req,arr[i],dep[j])
    if(arr[i]<=dep[j]):
        rooms_req+=1
        i+=1
    elif(dep[j]<arr[i]):
        rooms_req-=1
        j+=1
    ans=max(ans,rooms_req)
print(rooms_req)
 