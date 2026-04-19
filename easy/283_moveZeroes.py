def moveZeroes(nums:list)->None: #哈希
    temp=[]
    for i in range(len(nums)):
        if nums[i]==0:
            temp.append(i)
    for j in range(len(temp)):
        m=temp[j]
        nums.pop(m-j)
    for k in range(len(temp)):
        nums.append(0)
def moveZeroes(nums:list)->None: #双指针
    if 0 in nums:
        i=nums.index(0)
        j=i+1
    else:
        return
    while j<len(nums) and nums[j]==0:
        j+=1 # 找到i后面第一个不为0的元素
    while j<len(nums) and i<j:
        nums[i]=nums[j]
        nums[j]=0
        if 0 in nums[i+1:]:
            i=nums[i+1:].index(0)+i+1
            j=i+1
            while j<len(nums) and nums[j]==0:
                j+=1
def moveZeroes(nums:list)->None:
    if 0 not in nums:
        return
    l=len(nums)
    i=0
    j=0
    while j<l:
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1

        

nums=[0,1,0,3,9]
moveZeroes(nums)
print(nums)
nums=[0,1,0,0,12]
moveZeroes(nums)
print(nums)
nums=[-1,1,0,0,12]
moveZeroes(nums)
print(nums)