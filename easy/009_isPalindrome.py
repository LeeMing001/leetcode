def isPalindrome(x:int)->bool:
    if x<0:
        return False
    s=str(x)
    i,j=0,len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
def isPalindrome(x:int)->bool:
    if x<0:
        return False
    s1=str(x)
    s_list=list(s1)
    s_list.reverse()
    s2=''.join(s_list)
    print(s1,s2)
    return s1==s2
def isPalindrome(x:int)->bool:
    if x<0:
        return False
    x_list=[]
    
    while x>0:
        x_list.append(x%10)
        x=x//10

    i,j=0,len(x_list)-1
    print(x_list)
    while i<j:
        if x_list[i]!=x_list[j]:
            return False
        i+=1
        j-=1
    return True
def isPalindrome(x:int)->bool:
    

x=101010
print(isPalindrome(x))