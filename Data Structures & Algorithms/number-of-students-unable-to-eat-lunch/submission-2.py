from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        sandwiches = deque(sandwiches)
        students = deque(students)

        declined = 0
        while sandwiches:
            topSandwich, topStudent = sandwiches[0], students[0]
            if topSandwich == topStudent:
                declined = 0
                sandwiches.popleft()
                students.popleft()
                continue
            else:
                declined += 1
                if declined == len(students): return len(students)
                students.append(students.popleft())
        return 0
        