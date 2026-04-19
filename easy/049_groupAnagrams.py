import hashlib
import copy
def groupAnagrams(strs:list[str])->list[list[str]]:
    # 先将每一个字符串按顺序重新排列，然后计算md5值的列表，它的md5列表的长度是返回列表的长度
    # 然后每个字符串放到md5长度列表中
    md5_list=[]
    str_temp=copy.deepcopy(strs)
    res_list=[]
    print()
    for i,ele_str in enumerate(str_temp):
        str_temp[i]=''.join(sorted(ele_str))
        md5_hash=hashlib.md5(str_temp[i].encode('utf-8')).hexdigest()
        if md5_hash not in md5_list:
            md5_list.append(md5_hash)
            res_list.append([strs[i]])
        else:
            t=md5_list.index(md5_hash)
            res_list[t].append(strs[i])
    return res_list
def groupAnagrams(strs:list[str])->list[list[str]]:
    str_dict={}
    for ele_str in strs:
        k=''.join(sorted(ele_str))
        if k in str_dict:
            str_dict[k].append(ele_str)
        else:
            str_dict[k]=[ele_str]
    return list(str_dict.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res_list=groupAnagrams(strs)
print(res_list)

