'''
[문제]:N과M(5) / 순열, 인덱스
'''

def back(s, n, m, buf,n_buf):
    
    if len(buf)==m:
        print(*buf)
        return


    for i in range(s, n+1):
        if n_buf[i-1] not in buf:
            buf.append(n_buf[i-1])
            back(s, n, m, buf, n_buf)
            buf.pop()

n, m = map(int, input().split(' '))
n_buf = sorted(list(map(int, input().split(' '))))

back(1,n,m,[], n_buf)
