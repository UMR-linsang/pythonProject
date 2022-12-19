# num=int(input("请输入一个整数:"))
# while(num!=0):
#     print(num%10,end='')
#     num=num//10



# a=int(input('请输入一个自然数x：'))
# # 十进制转二进制 (bin)
# b=bin(a)
# print('它的二进制是:',b)
# # 十进制转换为八进制  (oct)
# c=oct(a)
# print('它的八进制是',c)
# # 十进制转换为十六进制 (hex)
# d=hex(a)
# print('它的十六进制是',d)



# n=int(input("请输入一个数N："))
# sum=0
# for i in range(n):
#     sum+=i+1
# print('1到N之间的和为',sum)



b=float(input('请输入本金：'))
r=float(input('请输入年利率：'))
n=int(input('请输入年份：'))
v=round(float(b*((1+r)**n)),2)
print('你的本金为',b,'年利率为',r,'年份为',n,'你的收益为',v)
