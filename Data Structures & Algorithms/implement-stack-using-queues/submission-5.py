from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 =  deque()

    def push(self, x: int) -> None:
        if  len(self.q1) == 0:
            self.q2.append(x)
        else:
            self.q1.append(x)


    def pop(self) -> int:
        if  len(self.q1) == 0 :
            
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            temp = self.q2[-1]
            self.q2 = []
            return temp
        else :
            while len(self.q1) >1:
                self.q2.append(self.q1.popleft()) 
            temp = self.q1[-1]
            self.q1 = []
            return temp

    def top(self) -> int:
        if not self.q1:
            return self.q2[-1]
        else:
            return self.q1[-1]

    def empty(self) -> bool:
        if len (self.q1) == 0  and  len(self.q2) ==0 :
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()