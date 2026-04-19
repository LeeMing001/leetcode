def maxArea(height:list[int])->int:
    i,j=0,len(height)-1
    max_area=0
    while i<j:
        #当前面积
        area=(j-i)*min(height[i],height[j])
        max_area=max(area,max_area)
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return max_area
   
height=[1,1]
print(maxArea(height))
height=[1,8,6,2,5,4,8,3,7]
print(maxArea(height))
height=[8,7,2,1]
print(maxArea(height))

        
