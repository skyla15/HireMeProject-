class listStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty() :
            print('Stack Empty')
        else :
            return self.stack.pop()

    def size(self):
        if self.isEmpty() :
            print('Stack Empty')
        else :
            return len(self.stack)

    def top(self):
        if self.isEmpty() :
            print('Stack Empty')
        else:
            return self.stack[-1]

    def isEmpty(self):
        return not bool(self.stack)

    def print_(self):
        if self.isEmpty() :
            print('Stack Empty')
        for s in self.stack :
            print(s, end= ' ')


def pushBracket(bracket) :
    stack = listStack()
    for c in bracket :
        if c in ('{', '[', '(') :
            stack.push(c)
            print('push push')
        elif c in ('}', ']', ')') :
            print('right', c)
            if stack.isEmpty() :
                return False
            else :
                left = stack.pop()
                if ( left == '{' and c != '}' ) or \
                        ( left == '(' and c != ')' ) or \
                        ( left == '[' and c != ']' ) :
                    return False

    print()
    print('stack check')
    print(stack.print_())
    print()

    return stack.isEmpty() # 갯수 안맞는 경우


if __name__ == '__main__' :
    str = ( '{ A[(i+1)] = 0;}', 'if(i ( i == 0 ) && ( j == 0 )' )
    for s in str :
        m = pushBracket(s)
        print(s, ' -->' , m)






