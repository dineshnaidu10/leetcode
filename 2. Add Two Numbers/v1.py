# ou are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)  # or current.data, depending on your class
        current = current.next
    return result

    def list_to_listnode(arr):
        if not arr:
            return None
        
        # Create a dummy node to act as the starting point
        dummy = ListNode(0)
        current = dummy
        
        # Iterate through the array and link new nodes
        for val in arr:
            current.next = ListNode(val)
            current = current.next
            
        # Return the first real node (skipping the dummy)
        return dummy.next

    l1 = list_node_to_list(l1)
    l2 = list_node_to_list(l2)
    l1 = int(''.join(map(str, l1)))
    l2 = int(''.join(map(str, l2)))
    l3 = l1 + l2
    l3 = [int(x) for x in str(l3)]

    return list_to_listnode(l3[::-1])
