# 비밀지도
# format, bin => 반환 : string!!!!!
def solution(n, arr1, arr2):
    secret_map = list()
    for i in range(n):
        # secret_map.append(format((arr1[i] | arr2[i]), 'b'))
        secret_map.append(bin(arr1[i] | arr2[i])[2:])
        secret_map[i] = '0' * ( n - len(secret_map[i]) ) + secret_map[i]
        secret_map[i] = ''.join(['#' if x == '1' else ' ' for x in secret_map[i]])
    return secret_map