def threeSum(nums:list[int])->list[list[int]]:
    l=len(nums)
    res_list=[]
    #先试试暴力解法
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if nums[i]+nums[j]+nums[k]==0:
                    temp=[nums[i],nums[j],nums[k]]
                    temp=sorted(temp)
                    if temp not in res_list:
                        res_list.append(temp)
    return res_list
def threeSum(nums:list[int])->list[list[int]]:
    nums=sorted(nums)
    res=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        j,k=i+1,len(nums)-1
        target=-nums[i]
        while j<k:
            if nums[j]+nums[k]>target:
                k-=1
            elif nums[j]+nums[k]<target:
                j+=1
            if j<k and nums[j]+nums[k]==target:
                temp=[nums[i],nums[j],nums[k]]
                res.append(temp)
                while k>j and nums[k-1]==nums[k]:
                    k-=1
                while j<k and nums[j+1]==nums[j]:
                    j+=1
                j+=1
    return res

        
nums=[-1,0,1,2,-1,-4]   
res=threeSum(nums)
print(res)             
nums=[0,0,0] 
res=threeSum(nums)
print(res)  
nums=[-2,0,0,2,2]
res=threeSum(nums)
print(res)  
nums=[-1,0,1,2,-1,-4]
res=threeSum(nums)
print(res) 
nums=[3,0,-2,-1,1,2]
res=threeSum(nums)
print(res) 

