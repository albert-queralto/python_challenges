from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

if __name__ == "__main__":
    pass
    # Example 1
    # Input: 1 -> 1 -> 2
    # Output: 1 -> 2
    # Explanation: 1 and 1 are duplicates, so we remove one of them.
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    result = delete_duplicates(head)
    while result:
        print(result.val)
        result = result.next
    
    # Example 2
    # Input: 1 -> 1 -> 2 -> 3 -> 3
    # Output: 1 -> 2 -> 3
    # Explanation: 1, 3, and 3 are duplicates, so we remove one of each.
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    result = delete_duplicates(head)
    while result:
        print(result.val)
        result = result.next