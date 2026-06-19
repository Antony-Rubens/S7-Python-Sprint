class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._move_elements()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move_elements()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def _move_elements(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# Test Cases
q = MyQueue()

q.push(1)
q.push(2)
q.push(3)

print(q.peek())    # 1
print(q.pop())     # 1
print(q.peek())    # 2
print(q.empty())   # False
print(q.pop())     # 2
print(q.pop())     # 3
print(q.empty())   # True
