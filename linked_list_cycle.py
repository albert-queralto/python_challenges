class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

if __name__ == "__main__":
    # Test case 1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    assert hasCycle(head) == True

    # Test case 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert hasCycle(head) == True

    # Test case 3
    head = ListNode(1)
    assert hasCycle(head) == False