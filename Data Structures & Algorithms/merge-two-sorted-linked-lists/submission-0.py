# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = []

        while list1 is not None or list2 is not None:
            if list2 is None or (list1 is not None and list1.val < list2.val):
                newList.append(list1.val)
                list1 = list1.next
            else:
                newList.append(list2.val)
                list2 = list2.next
        
        temp = ListNode()
        current = temp

        for value in newList:
            current.next = ListNode(value)
            current = current.next

        return temp.next
            