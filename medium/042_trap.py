def trap(height:list[int])->int:
    #如果是一直递增，不行
    #如果一直递减，也不行
    #先递减，后递增是可以的
    stack_1=[] #递减的栈
    stack_2=[]
    res=0
    for i,e in enumerate(height):
        if not stack_1 and e<=0:
            continue
        print("i=",i)
        print("s_1:",stack_1)
        print("s_2:",stack_2)
        print("res",res)
        if stack_2:
            if  e>=stack_2[-1][0]:
                stack_2.append([e,i])
            else:
                before=stack_2[-1]
                h=min(stack_1[0][0],stack_2[-1][0])
                w=stack_2[-1][1]-stack_1[0][1]-1 #没包括最后一个
                tem_res=h*w+stack_1[0][0]+stack_2[-1][0]
                while stack_1:
                    t=stack_1.pop()[0]
                    tem_res-=t
                while stack_2:
                    tem_res-=stack_2.pop()[0]
                res+=tem_res
                stack_1.append(before)
                stack_1.append([e,i])
        else:
            if not stack_1 or e<=stack_1[-1][0]:
                stack_1.append([e,i])
            else:
                stack_2.append([e,i])
    return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
res=trap(height)
print(res)
print('-----------')
height = [4,2,0,3,2,5]
res=trap(height)
print(res)