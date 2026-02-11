class Solution:
    def quickSort(self, arr, low, high):
        #code here 
        if(low<high):
            p=self.partition(arr, low, high)
            self.quickSort(arr,low,p-1)
            self.quickSort(arr,p+1,high)
            
            

    def partition(self, arr, l, h):
        pivot=arr[l]
        i=l
        j=h
        while(i<j):
            while(i<h and arr[i]<=pivot):
                i+=1
            while(j>l and arr[j]>pivot):
                j-=1
            if(i<j):
                arr[i],arr[j]=arr[j],arr[i]
        arr[l],arr[j]=arr[j],arr[l]
        return j
        
        
        
