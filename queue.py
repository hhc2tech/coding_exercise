
'''
Queue using list 
attribute: tail, head 
Methods available:
    * push
    * pop 
    * top 
    * isempty 
'''

from __future__ import print_function
class Queue(object):
    def __init__(self):
        self.items = list()

    def enqueue(self, val):
        self.items.insert(0, val)

    def dequeue(self):
        self.items.pop()

def creatQueue(nums):
    """
    creat a stack based on nums, nums is a python list 
    """
    q = Queue() 
    for n in nums:
        q.enqueue(n)
    return q

# def test_linkedlist():
if __name__ == "__main__":
    q1 = creatQueue([])
    q2 = creatQueue([1])
    q3 = creatQueue([1, 2, 1])
    q4 = creatQueue([1, 2, 3, 2, 1])
    q5 = creatQueue([1, 2])
    q6 = creatQueue([1, 2, 3, 4, 2])
    print(q6.items)
    print(q6.dequeue())
    print(q6.items)
    print(q1.dequeue())