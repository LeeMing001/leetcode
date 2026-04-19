def twoSum(nums,target):#双循环
    for num in range(len(nums)):
        for t in range(num+1,len(nums)):
            if nums[num]+nums[t]==target:
                return num,t
    return (-1,-1)
def twoSum(nums,target):#改进的多次遍历
    for num in range(len(nums)):
        t=target-nums[num]
        if t in nums[num+1:]:
            return [num,nums[num+1:].index(t)+num+1]
    return (-1,-1)
def twoSum(nums,target):#哈希
    seen={}
    # 键值对，键是要找的数 值是位置
    for i,num in enumerate(nums):
        t=target-nums[i]
        if t in seen:
            return [seen[t],i]
        #如果没在
        seen[num]=i
    return [-1,-1]
def twoSum(nums,target):#双指针
    temp=nums.copy()
    temp.sort() #原地排序
    i=0         #左指针
    j=len(nums)-1 #右指针
    while i<j:
        if (temp[i]+temp[j])>target:
            j-=1
        elif (temp[i]+temp[j])<target:
            i+=1
        else:
            break
    if i==j:
        return [-1,-1]
    t1=nums.index(temp[i])
    nums.pop(t1)
    t2=nums.index(temp[j])
    if t2>=t1:
        t2+=1
    return [t1,t2] if t1<t2 else [t2,t1]
def twoSum(nums:list[int],target):
    for i,e in enumerate(nums):
        t=target-e
        if t in nums and i!=nums.index(t):
            return [i,nums.index(t)]


nums=[2,7,11,15]
target=9
a,b=twoSum(nums,target)
print(a,b)
nums=[3,2,4]
target=6
a,b=twoSum(nums,target)
print(a,b)
nums=[3,3]
target=6
a,b=twoSum(nums,target)
print(a,b)
nums=[0,3,-3,4,-2]
target=-2
a,b=twoSum(nums,target)
print(a,b)