# 노가다 문자열 비교가 필요하다 -> 해시
# - 문자열 해싱 : 라빈 카프 / KMP 알고리즘
# - 접두사 문제 : Trie
## 트라이 접목 문제 : https://www.crocus.co.kr/1053

# 답안 : https://deepwelloper.tistory.com/128
# 깊은 복사, 얕은 복사 활용
_end = '_end'
def trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            if _end in current_dict:
                return False
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return True

def solution(phone_book):
    phone_book.sort()
    return trie(phone_book)
