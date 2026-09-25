class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index ==0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        temp = self.head.next
        self.head.next = new
        temp.prev = new
        new.prev = self.head
        new.next = temp
        return

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        temp = self.tail.prev
        self.tail.prev = new
        temp.next = new
        new.prev = temp
        new.next = self.tail
        return

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            new = ListNode(val)
            temp = curr.prev
            temp.next = new
            curr.prev = new
            new.prev = temp
            new.next = curr
        return

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)