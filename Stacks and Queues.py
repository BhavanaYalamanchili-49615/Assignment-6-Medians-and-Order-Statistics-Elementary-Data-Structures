# Both Stacks and Queues were implemented in Python lists in a combined way.
# The stack has a stack principle of the Last In First Out (LIFO), whereas the queue has a principle of the First In First Out (FIFO).
# Stack operations such as push, pop, peek were used and queue operations such as enqueue, dequeue, peek.

class Stack:
    def __init__(self):
        self.stack = []

    # Pushing a value onto the stack
    def push(self, value):
        self.stack.append(value)

    # Popping a value from the stack
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    # Viewing the top value of the stack
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None


class Queue:
    def __init__(self):
        self.queue = []

    # Enqueuing a value into the queue
    def enqueue(self, value):
        self.queue.append(value)

    # Dequeuing a value from the queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    # Viewing the front value of the queue
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return None

# Example usage:
stack = Stack()
# Pushing 5 onto the stack
stack.push(5)
# Pushing 10 onto the stack
stack.push(10)
# Popping the top element
print(stack.pop())

queue = Queue()
# Enqueuing 5 into the queue
queue.enqueue(5)
# Enqueuing 10 into the queue
queue.enqueue(10)
# Dequeuing the front element
print(queue.dequeue())