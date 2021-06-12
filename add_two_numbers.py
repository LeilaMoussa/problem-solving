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
    def append_to_list_util(self, lis: ListNode, new_node: ListNode):
        assert(new_node != None)
        if lis == None:
            lis = new_node
            assert(lis != None)
        else:
            walker = lis
            while walker.next:
                walker = walker.next
            walker.next = new_node
    
    def make_node(self, val1: int, val2: int, carry: int) -> (ListNode, int):
        # Oh! Happy day! That type-hint syntax for return types is fine!
        _sum = val1 + val2 + carry
        digit, carry = _sum % 10, _sum // 10
        return ListNode(digit), carry
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        first = True
        result = None
        while l1 and l2:
            new_node, carry = self.make_node(l1.val, l2.val, carry)
            # What the heck? Why doesn't this work in append_to_list_util()??
            if result == None:
                result = new_node
            else:
                self.append_to_list_util(result, new_node)
            assert(result != None)
            l1, l2 = l1.next, l2.next
        while l1:
            new_node, carry = self.make_node(l1.val, 0, carry)
            self.append_to_list_util(result, new_node)
            l1 = l1.next
        while l2:
            new_node, carry = self.make_node(0, l2.val, carry)
            self.append_to_list_util(result, new_node)
            l2 = l2.next
        if carry > 0:
            self.append_to_list_util(result, ListNode(carry))
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
    ans = sol.add_two_numbers(l1, l2)
    ans.display()

if __name__ == '__main__':
    main()
