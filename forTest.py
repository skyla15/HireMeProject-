# def make_set(arr):
#     new_set = list()
#     for e in arr:
#         if e not in new_set:
#             new_set.append(e)
#     return new_set
#
# def sum(base, other):
#     return [x for x in other if x not in base] + base
#
# def complement(base, other):
#     return [x for x in base if x not in other]
#
# def intersect(base ,other):
#     return [x for x in base if x in other]
#
# def main():
#     arrayA = [1,3,4,5,6,7,8,9,0,1,2,3,2,4,5,1]
#     arrayB = [10,2,3,4,7,12,3,4,2]
#     setA = make_set(arrayA)
#     setB = make_set(arrayB)
#
#     print('A   : ', setA)
#     print('B   : ', setB)
#     print('A+B : ', sum(setA, setB))
#     print('A-B : ', complement(setA, setB))
#     print('A^B : ', intersect(setA,setB))
#
# def main2():
#     print( sorted( ["가을", "우주", "너굴"] ))
#     print( sorted(["꿀꿀꿀", "꿀꿀", "꿀잠", "꿀"]))
#     print( sorted(["꿀꿀", "꿀", "잠잠잠", "잠"]))
# main2()


a = [1,2,3,4]
del a[3]
print(a)