from linked_list_utils import array_to_linked_list,print_linked_list,ListNode
from typing import Optional
def removeNthFromEnd(head: Optional[ListNode],n:int)->Optional[ListNode]:
    if head==None:
        return None
    p=q=head
    i=0
    if q.next==None and n==1:
        return None
    while i<n and q.next :
        q=q.next
        i+=1
    if i==n:
        while q.next:
            p=p.next
            q=q.next
        p.next=p.next.next
    elif i+1==n:
        p=p.next
        head=p
    return head
def removeNthFromEnd(head:Optional[ListNode],n:int)->Optional[ListNode]:
    if head==None:
        return None
    l_stack=[]
    p=head
    while p:
        l_stack.append(p)
        p=p.next
    for i in l_stack:
        print(i.val,end=" ")
    print()
    count=0
    while l_stack and count<n:
        l_stack.pop()
        count+=1
    for i in l_stack:
        print(i.val,end=" ")
    print()
    if not l_stack and count==n:
        return head.next
    p=l_stack.pop()
    p.next=p.next.next
    return head
def removeNthFromEnd(head:Optional[ListNode],n:int)->Optional[ListNode]:
    if head==None:
        return None
    l_stack=[]
    p=head
    while p:
        l_stack.append(p)
        p=p.next
    count=0
    while count<n and l_stack:
        l_stack.pop()
        count+=1
    if l_stack:
        p=l_stack.pop()
        p.next=p.next.next
    elif count==n:
        head=head.next
    #如果是空的，直接把head给出去
    return head
    
arr=[1,2,3,4,5]
head=array_to_linked_list(arr)
head=removeNthFromEnd(head,2)
print_linked_list(head)
arr=[1]
head=array_to_linked_list(arr)
head=removeNthFromEnd(head,2)
print_linked_list(head)
arr=[]
head=array_to_linked_list(arr)
head=removeNthFromEnd(head,1)
print_linked_list(head)
