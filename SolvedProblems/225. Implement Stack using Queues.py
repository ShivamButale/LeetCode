from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x) 

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        temp = self.queue1[0]
        self.queue1 = self.queue2
        self.queue2 = []
        return temp 

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        temp = self.queue1[0]
        self.queue1 = self.queue2
        self.queue1.append(temp)
        self.queue2 = []
        return temp 
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1)==0
