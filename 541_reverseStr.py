def reverseStr(s:str,k:int)->str:
    l=len(s)
    t=l//(2*k) #需要循环几次
    m=l-t*2*k
    if m>=k:
        r=True # 剩余大于等于k,小于2k，只反转前k个
    else : 
        r=False # 剩余长度小于k，需要全部反转
    for i in range(t):
        s_temp=s[i*2*k:i*2*k+k][::-1]
        s=s[:i*2*k]+s_temp+s[i*2*k+k:]
    if r:# 反转最后一段的前k个
        s_temp=s[t*2*k:t*2*k+k][::-1]
        s=s[:t*2*k]+s_temp+s[t*2*k+k:]
    else: #全部反转
        s_temp=s[t*2*k:][::-1]
        s=s[:t*2*k]+s_temp
    return s
def rever_list(s_list,left,right):
    while left<right:
            temp=s_list[left]
            s_list[left]=s_list[right]
            s_list[right]=temp 
            left+=1
            right-=1

def reverseStr(s:str,k:int)->str:
    l=len(s)
    s_list=list(s)
    t=l//(2*k) #需要正常旋转几趟
    if l-t*2*k>=k: #判断剩余的怎么做
        r=True   #反转前k个
    else:
        r=False  #剩余k个全部反转
    for i in range(t):
        left=i*k*2
        right=i*k*2+k-1
        rever_list(s_list,left,right)
        
    if r:# 反转最后一段的前k个
        left=t*k*2
        right=t*k*2+k-1
    else: #全部反转
        left=t*k*2
        right=l-1
    rever_list(s_list,left,right)
    return ''.join(s_list) 




s="abcdefg"
k=2
s=reverseStr(s,k)
print(s)
s="abcdefghij"
k=4
s=reverseStr(s,k)
print(s)
        