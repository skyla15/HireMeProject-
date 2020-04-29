import ArrayStack as AS

def is_matched_html(expr):
    S = AS.ArrayStack()
    j = expr.find('<')      # find the first index of '<'
    while j != -1:
        k = expr.find('>')  # find the next index of '>'
        if k == -1:
            return False    # Document is like this : < >, which is not valid.
        tag = expr[j+1:k]     # '<'[tag name]'>' , '<'[/tag name]'>'
        if not tag.startswith('/'):     # if not closing tag
            S.push(tag)
        else:                           # if closing tag
            if S.is_empty():            # invalid ( no opening tag found )
                return False
            if tag[1:] != S.pop():      # Compare opening tag with the next closing tag found
                return False            # if the names dont match, invalid
    return S.is_empty()
