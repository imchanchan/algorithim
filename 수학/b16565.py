'''
[문제]:N포커 // 조합
'''

def fac(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

import math

def comb(n, r):
    return math.comb(n, r)
    
# = = = = = =  = = = = = = 

N = int(input())

# 몫:a, 나머지:r 
res = 0


a = N//4 # 몫
for k in range(1,a+1):
    first = comb(13,k)
    second = comb(52-4*k, N-4*k) # N = 4*a + 4*na ?? 왜이렇게 하면 틀리는가..

    if k%2==1: ## 홀수일때
        res = res + (first * second)
    else :     ## 짝수일때
        res = res - (first * second)


print(res%10007)

