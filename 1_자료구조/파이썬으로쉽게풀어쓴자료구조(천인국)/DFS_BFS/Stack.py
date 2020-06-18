class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            print('Stack Empty')
            return
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.isEmpty() :
            print('Stack Empty')
            return