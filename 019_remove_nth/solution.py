class ListNode(object):
    def __init__(self, x, n):
        self.val = x
        self.next = n

    def __str__(self):
        return str(self.val) + " -> " + str(self.next)

def removeNthFromEnd(head, n):
    nAheadPtr = head
    currPtr = head
    nAhead = 0
    while (nAheadPtr != None and nAhead < n):
        nAhead = nAhead+1
        nAheadPtr = nAheadPtr.next

    if (nAheadPtr == None):
        return currPtr.next

    while(nAheadPtr.next != None):
        nAheadPtr = nAheadPtr.next
        currPtr = currPtr.next
    currPtr.next = currPtr.next.next
    return head

print(removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,None))))), 2)) #1->2->3->->5
print(removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,None))))), 5)) #"2->3->4->5->None"
print(removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,None))))), 1)) #"1->2->3->4->None"
print(removeNthFromEnd(ListNode(5, None), 1)) #"None"
