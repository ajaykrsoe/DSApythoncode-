#M1
def permutation(index,l):
    if(index<len(l)):
        for i in range(index,len(l)):
            t=l.copy()
            t[index],t[i]=t[i],t[index]
            permutation(index+1,t)

    else:
        print(''.join(l),end=" ")

s="ABCDE"
l=list(s)
permutation(0,l)





#M2
def permutation(index, arr):
    if index == len(arr):
        print(''.join(arr), end=" ")
        return

    for i in range(index, len(arr)):
        arr[index], arr[i] = arr[i], arr[index]
        permutation(index + 1, arr)
        arr[index], arr[i] = arr[i], arr[index]  # backtrack

s = "ABCDE"
permutation(0, list(s))

