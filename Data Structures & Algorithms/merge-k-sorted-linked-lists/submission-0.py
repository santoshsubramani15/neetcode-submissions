# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        x=[]
        for  i in lists:
            current = i
            while current is not None:
                x.append(current.val)  
                current = current.next  
        x.sort()
        if not x:
            y = None
        else:
            dummy = ListNode(0)
            current = dummy
            for val in x:
                current.next = ListNode(val)
                current = current.next
            y = dummy.next
        return y