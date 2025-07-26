class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged_list_1 = mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged_list_1))  # Output: [1, 1, 2, 3, 4, 4]

    list3 = create_linked_list([])
    list4 = create_linked_list([])
    merged_list_2 = mergeTwoLists(list3, list4)
    print(linked_list_to_list(merged_list_2))  # Output: []

    list5 = create_linked_list([])
    list6 = create_linked_list([0])
    merged_list_3 = mergeTwoLists(list5, list6)
    print(linked_list_to_list(merged_list_3))  # Output: [0]