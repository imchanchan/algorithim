'''
[문제]:N과M(4) / backtracking
'''

n, m = map(int, input().split(' '))

def back(s, n, m, buf):
    for i in range(s, n+1):
    
        if len(buf)==m:
            print(*buf)
            return
        
        # 중복(O)
        buf.append(i)
        # print(buf)
        back(i, n, m, buf) # 순서(O) : (1,2,3) == (3,2,1) 
        buf.pop()
        # print(buf)




back(1,n,m,[])

