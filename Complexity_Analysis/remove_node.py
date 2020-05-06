# Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

# O(n)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        tmp = head
        numNodes = 0
        while tmp is not None:
            tmp = tmp.next
            numNodes += 1 
        k = numNodes - n 

        prev = None
        ptr = head
        while k != 0:
            prev = ptr
            ptr = ptr.next
            k -= 1
        
        if prev is None:
            return head.next
        else:
            prev.next = ptr.next
            ptr.next = None
            return head

        