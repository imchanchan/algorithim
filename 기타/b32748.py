'''
[문제]:f(A+B) / 수학
'''

li = list(map(int,input().split(' ')))
n, m = list(input().split(' '))

# [함수]
dic={}
for i in range(len(li)):
    dic[i] = li[i]

# [역함수]
r_dic = {v: k for k, v in dic.items()}

# print(n, m)
a=list(n)
a1=''
b=list(m)
b1=''
# print(a,b)

for i in a:
    a1+=(str(r_dic[int(i)]))

for i in b:
    b1+=(str(r_dic[int(i)]))

# print(a1, b1)

c = str(int(a1)+int(b1))
c1=''
for i in c:
    c1 += (str(dic[int(i)]))

print(int(c1))

