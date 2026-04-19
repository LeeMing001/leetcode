class ListNode:
    """力扣常用的链表节点定义"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    """
    将 Python 列表转换为链表
    :param arr: 列表，如 [1,2,3,4]
    :return: 链表的头节点
    """
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """
    打印链表的值，格式：1 -> 2 -> 3 -> None
    """
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values) + " -> None")

def linked_list_to_array(head):
    """
    将链表转换为 Python 列表（便于验证或断言）
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# 示例用法
if __name__ == "__main__":
    # 测试数组转链表
    test_array = [1, 2, 3, 4, 5]
    head = array_to_linked_list(test_array)
    
    print("原始数组:", test_array)
    print("转换后的链表:")
    print_linked_list(head)
    
    # 测试链表转回数组
    back_to_array = linked_list_to_array(head)
    print("链表转回数组:", back_to_array)
    
    # 验证空数组情况
    empty_head = array_to_linked_list([])
    print("空数组转链表:", empty_head)