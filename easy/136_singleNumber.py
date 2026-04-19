def singleNumber(nums:list[int])->int:
    nums_temp=sorted(nums)
    current_e=nums_temp[0]
    count=1
    for i,e in enumerate(nums_temp[1:],start=1):
        if current_e==e:
            count+=1
        elif count==1:
            break
        else:
            count=1
            current_e=e
    return current_e

def singleNumber(nums:list[int])->int:
    res=0
    for num in nums:
        res^=num
    return res
def singleNumber(nums:list[int])->int:
    # 出现2次不是出现多次
    while nums:
        k=nums.pop(0)
        if k in nums:
            nums.pop(nums.index(k))
        else:
            return k


            
        
nums=[6,2,2,1,1,3,3,8,8,6,5]
print(singleNumber(nums))
