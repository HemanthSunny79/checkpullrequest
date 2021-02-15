string="bababcdefghijklmnopqrstuvwxyz"
"""size=len(string)
dp=[[0 for i in range(26)] for j in range(size)]

i=0
while(i<size and string[i]!='a'):
    i+=1
#print(i,dp[0])
if(i<size):
    
    dp[i][0]=1
    i+=1
    while(i<size):
        num=ord(string[i])-97
        j=0
        is_zero=0
        while(j<26 and is_zero==0):
            if(j==num):
                if(j==0):
                    dp[i][j]=dp[i-1][j]+1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
            else:
                dp[i][j]=dp[i-1][j]
            if(dp[i][j]==0):
                is_zero=1
            j+=1
        
        i+=1
    print(dp,"\n")

print(dp[size-1][25])"""
#GFG better approach
# If last characters of two strings are same, 
#    1. We consider last characters and get count for remaining 
#       strings. So we recur for lengths m-1 and n-1. 
#    2. We can ignore last character of first string and 
#       recurse for lengths m-1 and n. ******important******
# else 
# If last characters are not same, 
#    We ignore last character of first string and 
#    recurse for lengths m-1 and n.
string="bababcdefghijklmnopqrstuvwxyz"
pattern="abcdefghijklmnopqrstuvwxyz"
m=len(string)
n=len(pattern)
dp=[[0 for i in range(n+1)] for j in range(m+1)]
#if pattern is empty
for i in range(m+1):
    dp[i][0]=1
#if string is empty
for j in range(n+1):
    dp[0][j]=0
for i in range(1,m+1):
    for j in range(1,n+1):
        if(string[i-1]==pattern[j-1]):
            dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
        else:
            dp[i][j]=dp[i-1][j]
print(dp[m][n])

