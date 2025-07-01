'''
[문제]:N과M(2) / backtracking
'''

n, m = map(int, input().split(' '))

def back(s, n, m, buf):

    for i in range(s, n+1):
    
        if len(buf)==m:
            print(*buf)
            return

        if i not in buf:    
            buf.append(i)
            # print(buf)
            back(i, n, m, buf)
            buf.pop()
            # print(buf)


back(1,n,m,[])
