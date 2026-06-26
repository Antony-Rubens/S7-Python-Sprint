stack = []
#push
stack.append('A')
stack.append('B')
stack.append('C')
#peek
topElement = stack[-1]
print("Top element of the stack is:", topElement)
# pop
stack.pop()
# Stack after pop
print("Stack is:", stack)
# to check if empty or not 
isEmpty = not bool(stack)
print("is Empty:", isEmpty)
#Size 
print("Size:",len(stack))