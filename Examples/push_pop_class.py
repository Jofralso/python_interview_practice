class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.apped(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if self.items:
            return self.items[-1]
        raise IndexError("Peek from empty stack")

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def clear(self):
        self.items = []
    


