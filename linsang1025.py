# def fact(a):
#     t=1
#     for i in range(1,a+1):
#         t*=i
#     return t
# n=int(input('请输入要求的n:'))
# s=0
# for i in range(1,n+1):
#     s+=fact(i)
# print('1!+2!+3!+..+%s!=%s'%(n,s))


def sum(n):
    def fact(a):
        t = 1
        for i in range(1, a + 1):
            t *= i
        return t
    s = 0
    for i in range(1, n + 1):
        s += fact(i)
    return s
n = int(input())
print('1!+2!+3!+..+%s!=%s'%(n,sum(n)))

