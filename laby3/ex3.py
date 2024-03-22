class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()

class QueueUsingStacks:
    def __init__(self):
        self.addStack = Stack()  # Stos do dodawania
        self.removeStack = Stack()  # Stos do usuwania

    def append(self, item):
        self.addStack.push(item)

    def extract(self):
        if self.empty():
            raise Exception("Queue is empty")
        if self.removeStack.empty():
            while not self.addStack.empty():
                self.removeStack.push(self.addStack.pop())
        return self.removeStack.pop()

    def empty(self):
        return self.addStack.empty() and self.removeStack.empty()

# Użycie
queue = QueueUsingStacks()
queue.append(1)
queue.append(2)
print(queue.extract())  # Wypisuje 1
print(queue.extract())  # Wypisuje 2
