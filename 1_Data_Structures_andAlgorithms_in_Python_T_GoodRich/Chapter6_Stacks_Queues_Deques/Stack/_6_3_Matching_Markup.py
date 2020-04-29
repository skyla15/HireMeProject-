import _6_0_ArrayStack as AS

def is_matched_html(expr):
    S = AS.ArrayStack()
    j = expr.find('<')      # find the first index of '<'
    while j != -1:
        k = expr.find('>', j+1)  # find the next index of '>'

        if k == -1:         # if the next '>' is at the end of the Markup Document,
            return False    # Document is '<  >', which is not valid. ( needs closing '>'

        # fetch tag name
        tag = expr[j+1:k]                             # '<'[tag name]'>' , '<'[/tag name]'>'

        # push opening tag name
        if not tag.startswith('/'):                   # if not closing tag
            print('opening tag1:{}'.format(tag))
            S.push(tag)

        # compare opening tag name and closing tag name
        else:                           # if closing tag
            print('closing tag1:{}'.format(tag))
            if S.is_empty():            # no matched opening tag found
                return False
            if tag[1:] != S.pop():      # Compare opening tag with the next closing tag found
                return False            # if the names don't match, invalid
        j = expr.find('<', k+1)
    return S.is_empty()



filename = 'test_6_3.txt'
expr =''
with open(filename) as f:
    for line in K:
        expr += line.rstrip()
    print(expr)

print(is_matched_html(expr))
