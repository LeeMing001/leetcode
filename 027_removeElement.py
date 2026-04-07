def removeElement(nums:list[int],val:int)->int:
    i=j=0
    l=len(nums)
    while j<l: #i左边是排序好没有val的，j右边是找第一个有的
        if nums[i]!=val:
            i+=1
        elif nums[j]!=val:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
    return i
def removeElement(nums:list[int],val:int)->int:
    nums_sorted=sorted(nums)
    l=len(nums)
    i,j=0,l-1
    if nums_sorted[i]>val or nums_sorted[j]<val:
        return j+1
    while i<j:
        if nums_sorted[i]<val:
            i+=1
        if nums_sorted[j]>val:
            j-=1
        if nums_sorted[i]==nums_sorted[j]==val:
            break
    count=j-i+1
    for t in range(count):
        nums_sorted.pop(i)
    nums[:]=nums_sorted[:]
    return l-(count)

nums=[1,3,2,3]
val=3
k=removeElement(nums,val)
print(k,nums)