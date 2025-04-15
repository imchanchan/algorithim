'''
[문제]: 너 봄에는 캡사이신이 맛있단다. / 조합
'''
N = int(input())
sort_spicy = sorted(list(map(int, input().split(' '))))

## [주의] : pow함수로 거듭제곱을 풀면, int 범위가 넘어간다. 
## pow함수 쓰지말고, 배열로 해결하자! 
p2 = [1] * (N + 1)
for i in range(1, N + 1):
    p2[i] = (p2[i - 1] * 2) % 1_000_000_007 ## 연산된 제곱 값마다 mod값을 취해, 범위를 줄여야한다!! 

res = 0
for i in range(len(sort_spicy)):

    a = (sort_spicy[(len(sort_spicy)-1)-i]-sort_spicy[i])
    b = p2[len(sort_spicy)-i-1]-1
    
    res += (a * b)%1_000_000_007
    
print(res%1_000_000_007)
