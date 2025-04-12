'''
[문제]:원
'''

def solution(r1, r2):
    answer = 0
    for i in range(0, r2+1): 
        for j in range(0, r2+1): 
            if (r1*r1) < (i*i + j*j) < (r2*r2):
                print((i,j))
                answer+=1
            
    # print(answer)
    return (answer*4 + 8)

print(solution(2,3))