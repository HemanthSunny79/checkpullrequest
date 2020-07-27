# We are given an array consisting of n elements. 
# At each operation you can select any one element and increase rest of n-1 elements by 1.
# You have to make all elements equal performing such operation as many times you wish.
# Find the minimum number of operations needed for this.
# operation | increased elements | after increment
#     1     |    1, 2            | 2, 3, 3
#     2     |    1, 2            | 3, 4, 3
#     3     |    1, 3            | 4, 4, 4

#O(n) approach gettig logic is tricky
# If we took a closer look at each operation as well problem statement 
# we will find that increasing all n-1 element except the largest one is similar to decreasing the largest element only. 
# So, the smallest elements need not to decrease any more and rest of elements will got decremented upto smallest one.
# In this way the total number of operation required for making all elements equal will be arraySum – n * (smallesteElement).
# Time complexity will be same as that of finding smallest elements and array sum i.e. O(n).

arr = [1, 5, 2, 1, 3, 2, 1]
m=min(arr)
s=sum(arr)
print(s-(len(arr)*m))