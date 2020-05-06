# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Input: 1->2->4, 1->3->4

#Create a new linked list:
# Output: 1->1->2->3->4->4

# O(1) 

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        ptr = head #reference to the head

        while True:
            if l1 is None and l2 is None:
                break #nothing to merge
            elif l1 is None:
                ptr.next = l2 
                break
            elif l2 is None:
                ptr.next = l1
            else:
                smallerVal = 0 
                if l1.val < l2.va:
                    smallerVal = l1.val
                    l1 = l1.next
                else:
                    smallerVal = l2.val
                    l2 = l2.next
                
                newNode = ListNode(smallerVal)
                ptr.next = newNode
                ptr = prt.next

            return head.next

