'''
[문제]:공원산책 / level 1
'''

from collections import deque

def next(direction, x, y):
    
    if direction == "E":
        nx = x+0
        ny = y+1
            
    if direction == "S":
        nx = x+1
        ny = y+0

    if direction == "W":
        nx = x+0
        ny = y-1
    
    if direction == "N":
        nx = x-1
        ny = y+0
    
    return [nx, ny]


def solution(park, routes):
    
    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == 'S':
                s = [x,y]
              
    print(s[0], s[1])
    
    for route in routes:
        
        direction, d_time = route.split(' ')
        
        x, y = s[0], s[1]
        
        for i in range(int(d_time)):
            
            nx, ny = next(direction, s[0], s[1])
            
            if nx>len(park)-1 or ny>len(park[0])-1 or nx<0 or ny<0 or park[nx][ny] == 'X':
                s[0] = x
                s[1] = y
                break
                        
            else:   
                s[0] = nx
                s[1] = ny
    
    
    answer = [s[0],s[1]]
    return answer