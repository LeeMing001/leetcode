def containsDuplicate(nums:list[int])->bool:
    dict={}
    for i,ele in enumerate(nums):
        if ele in dict:
            return True
        else:
            dict[ele]=1
    return False
def containsDuplicate(nums:list[int])->bool:#数据集中时可以使用，数据分散时占用空间比较多
    max_e=max(nums)
    min_e=min(nums)
    temp_list=[0]*(max_e-min_e+1)
    for i,ele in enumerate(nums):
        if temp_list[ele-min_e]>0:
            return True
        else:
            temp_list[ele-min_e]+=1
    return False
def containsDuplicate(nums:list[int])->bool:
    nums_t=sorted(nums)
    if len(nums)<=1:
        return False
    before_e=nums[0]
    for i ,ele in enumerate(nums_t[1:],start=1):
        if ele ==before_e:
            return True
        before_e=ele
    return False
def containsDuplicate(nums:list[int])->bool:
    st=set()
    for e in nums:
        if e in set():
            return True
        st.add(e)
    return False
nums=[1,2,4,2]
print(containsDuplicate(nums))
