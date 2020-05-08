from collections import defaultdict

def groupWords(words):
    group = defaultdict()
    print(group.__getitem__(0))
    print(group)
    # grouper = defaultdict(list)
    # for word in words:
    #     length = len(word)
    #     grouper[length].append(word)
    # print(grouper.__getitem__(2))
    # print(grouper)

words=['galway', 'galway', 'my', 'girl']
groupWords(words)
# defaultdict(<class 'list'>, {6: ['galway', 'galway'], 2: ['my'], 4: ['girl']})