from typing import Optional
from linked_list_utils import array_to_linked_list,print_linked_list,ListNode
def getIntersectionNode(self,headA:ListNode,headB:ListNode)->Optional[ListNode]:
    if headA==None or headB==None:
        return None
    l_a=0
    l_b=0
    List_a=headA
    List_b=headB
    while List_a or List_b:
        if List_a:
            l_a+=1
            List_a=List_a.next
        if List_b:
            l_b+=1:
            List_b=List_b.next
    List_a,List_b=headA,headB
    while l_a!=l_b:
        if l_a>l_b:
            l_a-=1
            List_a=List_a.next
        else:
            l_b-=1
            List_b=List_b.next
    while List_a!=List_b:
        List_a=List_a.next
        List_b=List_b.next
    return List_a
            
