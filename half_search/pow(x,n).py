def solution(x, n):
    '''
    :param x:  底
    :param n:  幂
    :return:   底的幂次方
    '''
    ans = 1
    i = abs(n)
    while i != 0:
        if i % 2 != 0:      # 当幂为奇数时，取出一个无法进行相乘的数进行运算
            ans *= x
        x *= x
        i //= 2
    return ans if n > 0 else 1 / ans
if __name__ == '__main__':
    res = solution(2, 11)
    print(res)