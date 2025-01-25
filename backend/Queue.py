class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    if len(self.queue) == 0:
      return None
    
    return self.queue.pop(0)

  def isEmpty(self):
    if len(self.queue) == 0:
      return True
    
    return False
    
  def peek(self):
    if len(self.queue) == 0:
      return None
    
    return self.queue[0]
  
  def rear(self):
    if len(self.queue) == 0:
      return None
    
    return self.queue[-1]
  
  def size(self):
    return len(self.queue)
  
  def display(self):
    return self.queue
  

if __name__ == "__main__":
  q = Queue()

  q.enqueue(10)
  q.enqueue(20)
  q.enqueue(30)

  print("Queue:", q.display())       # Output: Queue: [10, 20, 30]
  print("Front:", q.peek())          # Output: Front: 10
  print("Rear:", q.rear())           # Output: Rear: 30
  print("Dequeue:", q.dequeue())     # Output: Dequeue: 10
  print("Queue after dequeue:", q.display())  # Output: Queue after dequeue: [20, 30]
  print("Is Empty:", q.isEmpty())    # Output: Is Empty: False
  print("Size:", q.size())           # Output: Size: 2