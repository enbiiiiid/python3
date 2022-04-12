# 徐也的猪
# 开发时间:2022/4/12   11:04
n=int(input('输入n'))
m=input('输入m')
l=list()
s=0
for i in range(n):
    for x in str(i):
       s+=int(x)
    l.append(s)
    s=0
l.sort()
print(l[int(m)])
