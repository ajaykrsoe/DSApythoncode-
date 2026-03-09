'''
heap = [0 for i in range(101)]  # our heap to be used
'''
#Function to insert a value in Heap.
def heapify(i) :
        minIndex=i
        leftIndex=minIndex*2+1
        rightIndex=leftIndex+1
        if(leftIndex<curr_size and heap[leftIndex]<heap[minIndex]) :
                minIndex=leftIndex
        if(rightIndex<curr_size and heap[rightIndex]<heap[minIndex]) :
                minIndex=rightIndex
        if(i!=minIndex) :
               heap[i],heap[minIndex]=heap[minIndex],heap[i]
               heapify(minIndex)
               
            
    
                 
def insertKey (x):
    global curr_size
    heap[curr_size]=x
    child=curr_size
    curr_size+=1
    parent=(child-1)//2
    while(child>0) :
        if(heap[parent]>heap[child]) :
            heap[parent] ,heap[child]=heap[child],heap[parent]
            child=parent
            parent=(child-1)//2
        else : 
            break
    

#Function to delete a key at ith index.
def deleteKey (i):
    global curr_size
    curr_size-=1
    temp=heap[i]
    heap[i]=heap[curr_size]
    if(heap[i]>=temp) :
        heapify(i)
    else :
        while(i>0 and heap[i] <  heap[(i-1)//2] ) :
            heap[i],heap[(i-1)//2]  =heap[(i-1)//2]  ,heap[i]
            i=(i-1)//2
            
    

    

#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    global curr_size
    if(curr_size== 0) :
        return -1
    curr_size-=1
    temp=heap[0]
    heap[0]=heap[curr_size]
    heapify(0)
    return temp
    
    
    


