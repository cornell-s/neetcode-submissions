# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = []
        while head is not None:
            
            newList.insert(0, head.val)
            head = head.next
        
        temp = ListNode()
        current = temp

        for value in newList:
            current.next = ListNode(value)
            current = current.next

        return temp.next
