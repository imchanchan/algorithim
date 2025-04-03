'''
[문제]:N과M / backtracking
'''

def dfs(start, n, m, buf):

    if len(buf) == m:
        print(*buf)

    for i in range(start, n+1):
        # print(buf)

        if i not in buf:
            # print(i)

            buf.append(i)

            dfs(start, n, m, buf)

            buf.pop()
    
    
N, M = map(int, input().split())

dfs(1,N,M,[])