class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
def hasCycle(head:Optional[ListNode])->bool:
    p=head
    while p:
        if hasattr(p,'is_read'):
            return True
        else:
            setattr(p,"is_read",True)
        if p.next:
            p=p.next
        else:
            break
    return False
def hasCycle(head:Optional[ListNode])->bool:
    # 可以使用快慢指针么，可以，且快指针一次应该是2，不能是3，why？
    # 因为两个指针相对运动差距为1，一次差1，那么距离每次减少1 ，一定会减少到0，不会跳过0
    # 可以使用栈么，感觉不行，因为链表长度很长可能，栈会很大。还有链表中的数值是可以重复的
    p=head
    if not p.next:
        return False
    else:
        q=head.next
    count=0
    while q:
        if count%2==0:
            p=p.next
        if p==q:
            return True
        q=q.next
        count+=1
    return False
    
        
