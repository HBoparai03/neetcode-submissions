# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
      
        first = head
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None

        second = slow
        end = None

        while second is not None:
            temp = second.next
            second.next = end
            end = second
            second = temp

        first, second = head, end
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            last = second
            first, second = tmp1, tmp2
        if second:
            last.next = second
            
        






        
        