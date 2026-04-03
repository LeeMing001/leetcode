import string
def isPalindrome(s:str)->bool:
    to_remove = string.whitespace + string.punctuation
    trans = str.maketrans('', '', to_remove)
    result = s.translate(trans)
    result=result.lower()
    i=0
    j=len(result)-1
    while i<=j :
        if result[i]==result[j]:
            i+=1
            j-=1
        else:
            return False
    return True
def isPalindrome(s:str)->bool:
    i=0
    j=len(s)-1
    l=len(s)
    while i<=j:
        while i<l and (not s[i].isalnum()) :
            i+=1
        
        while j>=0 and (not s[j].isalnum()) :
            j-=1
        if i<=j and s[i].lower()!=s[j].lower():
            return False
        i+=1
        j-=1
    return True


        

s= "252"

print(isPalindrome(s))
s= "a"

print(isPalindrome(s))
s= "   "

print(isPalindrome(s))
s= "r323k"

print(isPalindrome(s))
s= "@#.?"

print(isPalindrome(s))