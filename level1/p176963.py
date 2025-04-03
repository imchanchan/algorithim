'''
[문제]:프로그래머스 / level 1
'''

def solution(name, yearning, photo):
    
    answer = []

    score = {}
    for j in range(len(name)):
        score[name[j]] = yearning[j]

    for names in photo:
        
        res=0
        for a_name in names:
            if a_name in name:
                res+=score[a_name]
            
        answer.append(res)
    
        
    return answer