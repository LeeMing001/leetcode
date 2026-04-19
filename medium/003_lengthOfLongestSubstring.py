def lengthOfLongestSubstring(s:str)->int:
    #用哈希 ,也可以用数组来模拟哈希，因为只有有限个
    seen={}
    count=0
    i=j=0
    l=len(s)
    max_str=0
    while j<l:
        if s[j] in seen:
            n=seen[s[j]]
            seen[s[j]]=j
            if s[i]==s[j]:
                i+=1
            while i<n:
                del seen[s[i]]
                i+=1
            i=n+1
        else:
            count=j-i+1
            max_str=max(max_str,count)
            seen[s[j]]=j
        j+=1
    return max_str
def lenthOfLongestSubstring(s:str)->int:
    #能不能先转成列表，列表的好处是可以切片使用
    s_list=list(s)
    i,j=0
    l=len(s)
    #
    s_set=set()
    while j<l:
        if s_list[j] in s_set:
            if s_list[i]!=s_list[j]:
                s_list.discard(set(s_list[i]))
            i+=1

            i=s_set(s_list[j])+1

s="abcabcbb"
print(lengthOfLongestSubstring(s))
s="pwwkew"
print(lengthOfLongestSubstring(s))