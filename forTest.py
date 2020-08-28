element = None
s = list()

def push(element):
    s.append(element)

def pop():
    if empty():
        return False
    return s.pop()

def size():
    return len(s)

def empty():
    return size() == 0

def top():
    return s[-1]


push(1)
push(2)
push(3)

print(pop())
print(top())


