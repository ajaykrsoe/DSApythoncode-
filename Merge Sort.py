class Solution:
    def mergeTwoSortedArray(self,arr,l,m,h):
        temp1=arr[l:m+1:]
        temp2=arr[m+1:h+1:]
        n1=len(temp1)
        n2=len(temp2)
        i=0
        j=0
        k=l
        while(i<n1 and j< n2):
            if(temp1[i]<=temp2[j]):
                arr[k]=temp1[i]
                i+=1
            else :
                arr[k]=temp2[j]
                j+=1                
            k+=1
        while(i<n1 ) :
                arr[k]=temp1[i]
                i+=1
                k+=1
        while(j<n2):
                arr[k]=temp2[j]
                j+=1
                k+=1
            
            
    def mergeSort(self, arr, l, h):
        #code here
        if(l<h):
            m=(l+h)//2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, h)
            self.mergeTwoSortedArray(arr,l,m,h)
                
