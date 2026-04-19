def minSubArrayLen(target:int,nums:list[int])->int:
    l=len(nums)
    min_count=0
    for i in range(l):
        if nums[i]>target:
            return 1
        else:
            count=1
            temp_sum=nums[i]
            print(temp_sum)
            j=i+1
            while temp_sum<target and j<l:
                temp_sum+=nums[j]
                count+=1
                print(min_count,i,j,count,temp_sum)
                j+=1
            if temp_sum>=target:
                if min_count==0 or min_count>count:
                    min_count=count
            
    return min_count
    
def minSubArrayLen(target:int,nums:list[int])->int:
    cur_sum=0
    left=0
    min_count=float('inf')
    for right in range(len(nums)):
        cur_sum+=nums[right]
        while cur_sum>=target:
            min_count=min(min_count,right-left+1)
            cur_sum-=nums[left]
            left+=1
    return min_count if min_count!=float('inf') else 0
        
target=7
nums=[2,3,1,2,4,3]
print(minSubArrayLen(target,nums))
target=4
nums=[1,4,4]
print(minSubArrayLen(target,nums))
target=11
nums=[1,1,1,1,2,1,1]
print(minSubArrayLen(target,nums))
target=213
nums=[12,28,83,4,25,26,25,2,25,25,25,12]
print(minSubArrayLen(target,nums))
