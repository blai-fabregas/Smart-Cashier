class Stack:
  def __init__(self) -> None:
    self.stack = []
  
  def push(self, item):
    self.stack.append(item)

  def pop(self):
    if self.isEmpty():
      return None
    
    return self.stack.pop()

  def isEmpty(self):
    if len(self.stack) == 0:
      return True

    return False

  def peek(self):
    if self.isEmpty():
      return None
    else:
      return self.stack[-1]
    
  def size(self):
    return len(self.stack)
  
  def display(self):
    return self.stack
  

if __name__ == "__main__":
  stack = Stack()
  print(stack.isEmpty())
  stack.push(1)
  stack.push(2)
  print(stack.peek())
  stack.pop()
  print(stack.peek())
  print(stack.isEmpty())
  stack.push(3)
  print(stack.size())
  print(stack.display())
