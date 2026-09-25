class ListNode:
    def __init__(self, value: int):
        self.val = value
        self.next = None
        self.prev = None

class Queue:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index ==0:
            return curr.val
        return -1

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        temp = self.tail.prev
        self.tail.prev = new
        temp.next = new
        new.prev = temp
        new.next = self.tail
        self.size += 1
        return

    def deleteAtHead(self) -> None:
        new = self.head.next.next
        if new:
            new.prev = self.head
            self.head.next = new
            self.size -= 1
        return       
        
        

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Transform list queue
        sandwiches.reverse() 
        q_students = Queue()
        for i in range(len(students)):
            q_students.addAtTail(students[i])
        counter = 0
        while sandwiches and q_students and counter <= q_students.size:
            if q_students.head.next.val == sandwiches[-1]:
                sandwiches.pop()
                q_students.deleteAtHead()
                counter = 0
            else:
                temp = q_students.get(0)
                q_students.deleteAtHead()
                q_students.addAtTail(temp)
                counter += 1
        return q_students.size

    