def isValid(s:str)->bool:
    s_s=[]
    left_=['(','{','[']
    right_=[')','}',']']
    for i ,ele in enumerate(s):
        if ele in left_:
            s_s.append(ele)
        elif ele in right_:
            if len(s_s)==0:
                return False
            k=s_s.pop()
            p=left_.index(k)
            q=right_.index(ele)
            if p!=q :
                return False
    if len(s_s)==0:
        return True
    else: return False

s="{"
print(isValid(s))