
'''
Stack without using list 
attribute: tail
Methods available:
    * append 
    * pop 
    * top 
    * isempty 
'''

from __future__ import print_function
class Node(object):
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 

class Stack(object):
    def __init__(self):
        self.tail = None
        # self._tail = None

    def append(self, value):
        new_tail = Node(value, next = self.tail)
        self.tail = new_tail
    def isempty(self):
        return not self.tail 

    def pop(self):
        if self.isempty(): 
            raise ValueError('The stack is empty')
        res = self.tail.value 
        self.tail = self.tail.next 
        return res 

    def top(self):
        if self.isempty():
            raise ValueError('The stack is empty')
        return self.tail.value 


    def __str__(self):
        """
        return empty string if empty 
        return just the number if len = 1
        else return a -> b -> c ....
        don't use len 
        """
        cur = self.tail  
        if not cur: return ''
        if not cur.next: return str(cur.value)
        s = str(cur.value)
        cur = cur.next 
        while cur:
            s += ' -> ' + str(cur.value)
            cur = cur.next 

        return s 

def creatStack(nums):
    """
    creat a stack based on nums, nums is a python list 
    """
    l = Stack() 
    for n in nums:
        l.append(n)
    return l 

# def test_linkedlist():
if __name__ == "__main__":
    l1 = creatStack([])
    l2 = creatStack([1])
    l3 = creatStack([1, 2, 1])
    l4 = creatStack([1, 2, 3, 2, 1])
    l5 = creatStack([1, 2])
    l6 = creatStack([1, 2, 3, 4, 2])
    print(l6)
    print(l2.pop())
    print(l2)