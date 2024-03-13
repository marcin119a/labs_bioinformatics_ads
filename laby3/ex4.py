class MinStack:
    def __init__(self):
        self.stack = []  # Główny stos przechowujący elementy
        self.minStack = []  # Dodatkowy stos przechowujący minimalne elementy

    def push(self, x):
        self.stack.append(x)
        # Jeśli minStack jest pusty lub x jest mniejszy lub równy aktualnemu minimum, dodaj x do minStack
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        if self.stack:
            top = self.stack.pop()
            # Jeśli element na szczycie stosu jest równy elementowi na szczycie minStack, usuń go również z minStack
            if top == self.minStack[-1]:
                self.minStack.pop()
            return top
        else:
            raise Exception("Stack is empty")

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")

    def min(self):
        if self.minStack:
            return self.minStack[-1]
        else:
            raise Exception("Stack is empty")

# Użycie
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.min())  # Wypisuje -3
minStack.pop()
print(minStack.top())  # Wypisuje 0
print(minStack.min())  # Wypisuje -2
