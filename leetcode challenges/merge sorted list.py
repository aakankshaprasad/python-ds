# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = list()
        while (l1):
            list1.append(l1.val)
            l1 = l1.next;
        while (l2):
            list1.append(l2.val)
            l2 = l2.next;
        list1.sort()
        return list1
