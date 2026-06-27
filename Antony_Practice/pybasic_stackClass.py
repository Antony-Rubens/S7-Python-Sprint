class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")    
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    
    # create stack
mystack = Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')

print("the stack is :", mystack.stack)
print("Pop:", mystack.pop())
print("stack after pop:",mystack.stack)
print("peek:", mystack.peek())
print("is Empty:",mystack.isEmpty())
print("Size of Stack:", mystack.size())