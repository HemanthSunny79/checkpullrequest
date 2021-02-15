def findPermutations(string, index, n,count):
    if count==size:
        print(''.join(string[:size]),end=" ")
        return 1
    for i in range(index, n):
        string[index], string[i] = string[i], string[index]
        t=findPermutations(string, index + 1, n,count+1)

        string[index], string[i] = string[i], string[index]
string = list(input())
n = len(string)
size=n
count=0
findPermutations(string, 0, n,count)	



