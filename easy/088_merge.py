def merge(nums1:list[int],m:int,nums2:list[int],n:int)->None:
    l1=len(nums1)
    l2=len(nums2)
    if l2==0:
        return
    i=j=0
    t=0
    while i<m and j<n:
        if nums1[i+t]<=nums2[j]:
            i+=1
        else:
            nums1.insert(i+t,nums2[j])
            t+=1
            j+=1
    while j<n:
        nums1.insert(i+t,nums2[j])
        t+=1
        j+=1
    while len(nums1)>l1:
        nums1.pop(l1)

def merge(nums1:list[int],m:int,nums2:list[int],n:int)->None:
    i,j,t=m-1,n-1,m+n-1
    while j>=0:
        if i>=0 and nums1[i]>nums2[j]:
            nums1[t]=nums1[i]
            i-=1
        else :
            nums1[t]=nums2[j]
            j-=1
        t-=1


        


nums1=[4,5,8,0,0,0]
nums2=[2,5,6]
m=3
n=3
merge(nums1,m,nums2,n)
print(nums1)
        
        

    
        
    