class ListNode:
    def __init__(val=0,next=None):
        self.val=val
        self.next=next
def reverseList(head:Optional[ListNode])->Optional[ListNode]:
    #用栈的方法，内存占用比较大，需要循环两次，一次遍历链表一次创建链表
    temp_s=[]
    while head!=None:
        temp_s.append(head.val)
        head=head.next
    Head=None
    if temp_s:
        L=ListNode(temp_s.pop())
        Head=L
    while temp_s:
        L.next=ListNode(temp_s.pop())
        L=L.next
    return Head

def reverseList(head:Optional[ListNode])->Optional[ListNode]:
    #双指针
    p=head
    q=p.next
    temp=None
    while p:
        p.next=temp
        temp=p
        p=q
        q=p.next
    return temp
    
    
    


        