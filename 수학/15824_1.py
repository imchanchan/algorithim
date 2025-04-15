'''
[문제]: 너 봄에는 캡사이신이 맛있단다. / 조합
'''
N = int(input())
sort_spicy = sorted(list(map(int, input().split(' '))))

res = 0
## [주의] 이중 for문 쓰면, 시간초과납니다. -> 생각을 더해서 j를 i 꼴로 만들어주세요!
for i in range(1, len(sort_spicy)+1):
    for j in range(i+1,len(sort_spicy)+1):
        # print(j,i, len(sort_spicy[i:j])-1)
        res += (sort_spicy[j-1]-sort_spicy[i-1]) * pow(2,len(sort_spicy[i:j])-1)

print(res)


