class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next
    
    def display(self):
        # There's probably a cuter way of writing this
        if self:
            print(self.val)
            if self.next:
                self.next.display()

class Solution:
    def make_node(self, val1: int, val2: int, carry: int) -> (ListNode, int):
        # Oh! Happy day! That type-hint syntax for return types is fine!
        _sum = val1 + val2 + carry
        digit, carry = _sum % 10, _sum // 10
        return ListNode(digit), carry
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = walker = None
        while l1 and l2:
            new_node, carry = self.make_node(l1.val, l2.val, carry)
            # What the heck? Why doesn't this work in append_to_list_util()??
            if result == None:
                result = new_node
                walker = result
            else:
                walker.next = new_node
                walker = walker.next
            l1, l2 = l1.next, l2.next
        while l1:
            new_node, carry = self.make_node(l1.val, 0, carry)
            walker.next = new_node
            walker = walker.next
            l1 = l1.next
        while l2:
            new_node, carry = self.make_node(0, l2.val, carry)
            walker.next = new_node
            walker = walker.next
            l2 = l2.next
        if carry > 0:
            walker.next = ListNode(carry)
            walker = walker.next
        return result

def main():
    #l1 = ListNode(2, ListNode(4, ListNode(3)))
    #l2 = ListNode(5, ListNode(6, ListNode(4)))
    # 7 -> 0 -> 8
    #l1 = ListNode(0)
    #l2 = ListNode(0)
    # 0
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    sol = Solution()
    ans = sol.addTwoNumbers(l1, l2)
    ans.display()

if __name__ == '__main__':
    main()
