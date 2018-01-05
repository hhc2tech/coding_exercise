
'''
An unsorted linked list. Nothing fancy here.
Methods available:
insert(value): insert a value into the linked list
remove(value): remove the first occurrence of the value in the list.
                Raise ValueError if that value doesn't exist
Extra usage:
    __str__(self): return the linked list in the form: a -> b -> c ...
    is_palindrome: return true if the linked list is palindrome
    
'''

from __future__ import print_function
class Node(object):
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 

class LinkedList(object):
    def __init__(self):
        self.head = None
        # self._tail = None
        self.len = 0

    def insert(self, value):
        new_node = Node(value)
        cur = self.head 
        if not cur: 
            self.head = new_node 
        else: 
            while cur.next:
                cur = cur.next 
            cur.next = new_node 

        # while cur is not None:
        #     cur = cur.next 
        # cur.next = new_node 
        # self.len += 1 

    def remove(self, value):
        """
        remove the first 'value' if the list contains that value
        doing nothing o.w.
        if list is empty, ignore 
        if value == self.head, self.head = self.head.next 
        else: curr = curr.next untill curr.value == value 
        then prev.next = curr.next 
        """
        if self.head.value == value: 
            self.head = self.head.next 
            return 
        curr = self.head 
        prev = Node(0)
        prev.next = self.head 
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return 
            prev, curr = prev.next, curr.next 



    def __str__(self):
        """
        return empty string if empty 
        return just the number if len = 1
        else return a -> b -> c ....
        don't use len 
        """
        cur = self.head 
        if not cur: return ''
        if not cur.next: return str(cur.value)
        s = str(cur.value)
        cur = cur.next 
        while cur:
            s += ' -> ' + str(cur.value)
            cur = cur.next 

        return s 

    def __contains__(self, value):
        """
        check if value is in list
        """        
        # pass 
        curr = self.head 
        while curr:
            if curr.value == value: return True 
            curr = curr.next 
        return False 

    # def __len__(self):
    #     pass 

    # def __iter__(self):
    #     # yield from self._iter(self._head)
    #     pass

    # def _iter(self, node):
        # if node:
        #     yield node.value
        #     yield from self._iter(node.next)
    def is_palindrome(self):
        """
        Given a singly linked list, determine if it is a palindrome.
        """
        slow = fast = self.head 
        prev = None 
        while fast and fast.next:
            fast = fast.next.next 
            slow, prev, prev.next = slow.next, slow, prev 

        # if odd number of nodes, then fast is not None, fast.next is None 
        # if even number of nodes, both fast is None 
        if fast:
            slow = slow.next 

        while slow and prev:
            if slow.value != prev.value: return False 
            slow, prev = slow.next, prev.next 
        return True 

def creatList(nums):
    """
    creat a linked list based on nums, nums is a python list 
    """
    l = LinkedList() 
    for n in nums:
        l.insert(n)
    return l 

# def test_linkedlist():
if __name__ == "__main__":
    l1 = creatList([])
    l2 = creatList([1])
    l3 = creatList([1, 2, 1])
    l4 = creatList([1, 2, 3, 2, 1])
    l5 = creatList([1, 2])
    l6 = creatList([1, 2, 3, 4, 2])
    print(l1.is_palindrome())
    print(l2.is_palindrome())
    print(l3.is_palindrome())
    print(l4.is_palindrome())
    print(l5.is_palindrome())
    print(l6.is_palindrome())
    
