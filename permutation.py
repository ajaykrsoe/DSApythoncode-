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
