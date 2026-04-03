def reverseString(s:list[str])->None:
    i=0
    j=len(s)-1
    while i<j:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
def reverseString(s:list[str])->None:
    for i in range(len(s)//2):
        s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]


s = ["h","e","l","l","o"]
reverseString(s)
print(s)
s = ["H","a","n","n","a","h"]
reverseString(s)
print(s)