from typing import Optional
from linked_list_utils import array_to_linked_list,print_linked_list,ListNode

def mergeTwoLists(list1:Optional[ListNode],list2:Optional[ListNode])->Optional[ListNode]:
    p=list1
    q=list2
    #假设其中一个是空的
    if p==None:
        return q
    if q==None:
        return p
    #现在两个都不是空的
    dummy=ListNode(-1)
    new_list=dummy
    while p and q:
        if p.val<=q.val:
            new_list.next=p
            new_list=new_list.next
            p=p.next
        else:
            new_list.next=q
            new_list=new_list.next
            q=q.next
    if p :
        new_list.next=p
        
    if q:
        new_list.next=q
    return dummy.next
#用递归的方法再写一遍
def mergeTwoLists(list1:Optional[ListNode],list2:Optional[ListNode])->Optional[ListNode]:
    #如何递归
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1.val<=list2.val:
        list1.next=mergeTwoLists(list1.next,list2)
        return list1
    else:
        list2.next=mergeTwoLists(list1,list2.next)
        return list2

l1 = [1,2,5]
l2 = [0]
l1=array_to_linked_list(l1)
l2=array_to_linked_list(l2)
p=mergeTwoLists(l1,l2)
print_linked_list(p)