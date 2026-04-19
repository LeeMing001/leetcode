def removeDuplicates(nums:list[int])->int:
    before_ele=nums[0]
    location=[]
    for i,ele in enumerate(nums[1:],start=1):
        if ele==before_ele:
            location.append(i)
            print(i,ele)
        before_ele=ele

    for i in range(len(location)):
        nums.pop(location[i]-i)
    return len(nums)

def removeDuplicates(nums:list[int])->int:
    i=j=0
    l=len(nums)
    while j<l: 
        if nums[j]>nums[i]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        j+=1
    return i+1

nums=[1,1,2,5]
k=removeDuplicates(nums)
print(k,nums)


