class ListNode(object):
    def __init__(self, x, n):
        self.val = x
        self.next = n

    def __str__(self):
        return str(self.val) + " -> " + str(self.next)

def mergeTwoList(l1, l2):
    if (l1 is None and l2 is None):
        return None
    if (l2 is None):
        return l1
    if (l1 is None):
        return l2
    if (l2.val < l1.val):
        return mergeTwoList(l2, l1)
    currAnswer = l1
    ansRest = mergeTwoList(l2, l1.next)
    currAnswer.next = ansRest
    return currAnswer

print(mergeTwoList(ListNode(2, ListNode(3, None)), None)) #3-2-None
print(mergeTwoList(None, None)) #None
print(mergeTwoList(ListNode(2, None), ListNode(5, None))) #2->5
print(mergeTwoList(ListNode(2, ListNode(8, None)), ListNode(5, ListNode(7, None)))) #2-5-3-7


