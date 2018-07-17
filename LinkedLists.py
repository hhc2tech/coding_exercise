from __future__ import print_function
# import pdb

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

# class LinkedList(object):
    # def __init__(self, nums):
def createList(nums):
    """
    creat a linked list from a list
    """
    if not nums:
        return None
    dumm = curr = ListNode(0)
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dumm.next

def printList(head):
    if not head:
        print('empty list')
        return
    curr = head
    # pdb.set_trace()
    while True:
        if curr.next:
            print(str(curr.val) + '->', end="")
        else:
            # print('\n')
            print(str(curr.val))
            return
        curr = curr.next

def _printList():
    A = []
    B = [1]
    C = [1,2]
    D = [3, 2, 1]
    printList(createList(A))
    printList(createList(B))
    printList(createList(C))
    printList(createList(D))

def mergeKlists(lists):
    """
    merge k sorted lists
    example:
        lists = [[1,4,5],[1,3,4],[2,6]]
        then output: [1, 1, 2, 3, 4, 4, 5, 6]
    """
    # pass
    import heapq
    if not lists: return None
    q = []
    for i, l in enumerate(lists):
        if lists[i]:
            heapq.heappush(q, (lists[i].val, i))
            lists[i] = lists[i].next
    dumm = curr = ListNode(0)
    while q:
        val, i = heapq.heappop(q)
        curr.next = ListNode(val)
        curr = curr.next
        if lists[i]:
            heapq.heappush(q, (lists[i].val, i))
            lists[i] = lists[i].next
    return dumm.next

def _mergeKlists():
    lists = [createList([1, 4, 5]), createList([1, 3, 4]), createList([2, 6])]
    printList(mergeKlists(lists))

if __name__ == '__main__':
    # _printList()
    _mergeKlists()

