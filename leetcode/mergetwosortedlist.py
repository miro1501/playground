# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # Appending the remaining nodes of l1 or l2
        cur.next = l1 or l2
        return dummy_head.next

        

l1 = [1,2,3]
l2 = [2,3,4,5]
solution = Solution.mergeTwoLists(None, ListNode(l1), ListNode(l2))
