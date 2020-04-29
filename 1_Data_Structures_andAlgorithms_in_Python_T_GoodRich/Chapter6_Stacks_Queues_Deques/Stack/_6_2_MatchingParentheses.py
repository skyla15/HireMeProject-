import _6_0_ArrayStack as AS

def is_matched(expr):
    '''
        return True if all delimiters are properly matched
    '''
    lefty = '({['
    righty = ')}]'

    S = AS.ArrayStack()
    for c in expr:          # O(n)
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if lefty.index(S.pop()) != righty.index(c):
                # lefty and righty should be declared in the matching order
                return False
    return S.is_empty()
    # Were all symbols matched?
    # 오른쪽 괄호들과 다 비교를 하였음에도 왼쪽 괄호가 계속 남아있을 경우 False


def matchingParentheses():
    with open('test_6_1_2.txt') as f:
        for line in f:      # O(n)
            if not is_matched(line):
                print('False')
                return

    print('Success')


matchingParentheses()

