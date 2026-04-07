def isAnagram(s:str,t:str)->bool:
    # 哈希的方式，存储字母和次数
    # 由于s和t只包含小写字母，最多有26位
    l1=len(s)
    l2=len(t)
    if l1!=l2:
        return False
    seen=[0]*26
    for s_i in (s):
        seen[ord(s_i)-97]+=1
    for t_i in (t):
        seen[ord(t_i)-97]-=1
    return set(seen)=={0}
def isAnagram(s:str,t:str)->bool:
    # 哈希的方式，存储字母和次数
    # 由于s和t只包含小写字母，最多有26位
    l1=len(s)
    l2=len(t)
    if l1!=l2:
        return False
    seen=[0]*26
    for s_i,t_i in zip(s,t):
        seen[ord(s_i)-97]+=1
        seen[ord(t_i)-97]-=1
    return set(seen)=={0}
s="abcd"
t="bcad"
print(isAnagram(s,t)) 
def isAnagram(s:str,t:str)->bool:
    # 哈希的方式，存储字母和次数
    # 由于s和t只包含小写字母，最多有26位，
    seen=[0]*26
    l1=len(s)
    l2=len(t)
    if l1!=l2:
        return False
    for i in range(len(s)):
        seen[ord(s[i])-97]+=1
        seen[ord(t[i])-97]-=1  
    return set(seen)=={0}
s="abcd"
t="bcud"
print(isAnagram(s,t))     
    
#将字符串列表化，然后排序，看两个列表是否完全相等
def isAnagram(s:str,t:str)->bool:
    s_list=list(s)
    t_list=list(t)
    s_list=sorted(s_list)
    t_list=sorted(t_list)
    return s_list==t_list

s="abcd"
t="bcad"
print(isAnagram(s,t))
