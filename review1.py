# 一、写一个转换字符串的函数
# 将输入字符串中下标为偶数的字符连成一个新的字符串输出，需要注意两点：
# 1. 如果输入字符串的长度超过20，则转换失败，返回“ERROR！”字符串；
# 2. 输入字符串只能由0-9数字，小写a-z和大写A-Z组成，如果包含其他字符，则转换失败，返回“ERROR！”字符串。
a= 'hfdkjasRTYUEWTQ4723618##+'
b = list(a)
# digit: 0-9 48-57
# not cap 97-122
# cap 65-90

f =  0
def rec(a):
    if a == "":
        return ""
    if (a[0].isalnum()):
        global f
        f = 1
        d = rec(a[2:])
    else:
        d = rec(a[2:])
    return d+a[0]


c = rec(a[1:])[::-1]
    # d =reversed(c)
# print(list(d))
if f:
    print('error')
else:
    print(c)

# 二、给定一个正整数，给出消除重复数字以后最大的整数
# 2.1 题目描述
# 给定一个正整数，给出消除重复数字以后最大的整数，注意需要考虑长整数。
#
# 输入示例：423234
# 输出示例：432
a = 423234
def e(a,r):
    if a<1:
        return
    b = a % 10
    r[b] = 1
    e(a//10,r)
r = {}
e(a,r)
s = list(r.keys())
s.sort(reverse = False)
a = 0
for index in range(len(s)):
    #print(s[index])
    #print(pow(10,index))
    a+= pow(10,index)*s[index]
    #print(a)
print(a)
# a= [3,4,2]
# a.sort(reverse=True)
# print(a)

# c = input("in")
# print(c)

# 三、实现2-62进制任意两种进制之间的转换
# 3.1 题目描述
# 将一个处于Integer类型聚会范围内的整数从指定源进制转换成指定目标进制；可指定的进制值范围为[2-62]；每个数字的可聚会范围为[0-9a-zA-Z];输出字符串的每一个都须为有效值，反例：”012”的百位字符为无效值，实现时无需考虑非法输入。
#
# 输入描述：源进制 目标进制 待转换的整数值
# 输入示例：8 16 12345670
# 输出示例：29cbb8
# 3.2 题目分析
# 先将进制值与字符值、字符值与进制值之间的转换函数写好；
# 两种进制之间的转换，一般是先将源进制转换成十进制，然后再转换成新进制；
# 另外需要注意输出是否为有效值。
d = int('12345670',8)
print(d)
# waiting to be solved
print(c)

# 题目：
#
# 输入一个整数（含负数），输出3个数据，如下：
# 1.输出该整数的位数;
# 2.将该整数各位拆分输出，中间以空格隔开（注意末位不能有空格）。如果是负数，则符号与第一个数一起输出；
# 3.输出该数的反转数，如为负数，符号位置不变，置于最前。
# 示例
# 输入：
#
# -12345
# 输出：
#
# 5
# -1 2 3 4 5
# -54321


# 第二题
# 题目：
#
# 输入4个IP值组成两个IP段：
# 第一、二行分别为第一个IP段的起始和结尾IP，第三、四行为第二个IP段的起始和结尾。
# 要求输出：
# 若两个IP段有交集则输出"Overlap IP"，没有则输出"No Overlap IP"。
# 示例
# 输入：
#
# 1.1.1.1
# 255.255.255.255
# 2.2.2.2
# 3.3.3.3
# 输出：
#
# Overlap IP

# ip1 = input().split('.')
# ip2 = input().split('.')
# ip3 = input().split('.')
# ip4 = input().split('.')
# print(ip1)
# print(ip2)
# print(ip3)
# print(ip4)

# case1: 1,2 constains 3 or 4
# case2: 3,4 contrains 1 or 2
def con(ip1,ip2,ip3,ip4):
    # case1
    return contains(ip1,ip2,ip3) or contains(ip1,ip2,ip4) or contains(ip3,ip4,ip1) or contains(ip3,ip4,ip2)
def contains(ip1, ip2, ip3):
    # case1
    r1 = []
    r1.append(comp(ip1[0],ip2[0],ip3[0]))
    r1.append(comp(ip1[1],ip2[1],ip3[1]))
    r1.append(comp(ip1[2],ip2[2],ip3[2]))
    r1.append(comp(ip1[3],ip2[3],ip3[3]))
    if r1.__contains__(False):
        return False
    return True

def comp(p1,p2,p3):
    if p1 > p3 or p3 > p2:
        return False
    else:
        return True
ip1='1.1.1.1'.split(".")
#ip2 ='255.255.255.255'
ip2 = '2.2.2.255'.split(".")
ip3='2.2.2.2'.split(".")
ip4 = '3.3.3.3'.split(".")
x = con(ip1,ip2,ip3,ip4)
print(x)
# c = contains(ip1,ip2,ip3)
# print(c)
# if c.__contains__(False):
#     print("hi")
# ip0 = 0
# for i in range(len(ip1)):
#     ip0+= pow(255,i)*ip1[i]
# print(ip0)

# 第三题
# 题目：
#
# 输入两行数据，第一行包含多个正整数，以空格分开，根据每个数的后三位大小进行排序；第二行为数值n,输出排序后指定位置n的数。
# 要求：
# 1.若数不足三位，则直接比较；
# 2.若两数比较结果相等，则两数相对位置不变。
# 要求输出：
# 排序后第n个数（位置从1开始）。
# 示例
# 输入：
#
# 12 450 9001 5231 8231 7231
# 5
# 输出：
#
# 7231

m = "12 450 9001 5231 8231 7231".split(" ")
p = 5
from collections import defaultdict
d = defaultdict(list)
for x in m:
    if len(x)>3:
        # if x not in d.keys():
        #     d[int(x[-3:])] = [x[:-3]]
        #     continue
        d[int(x[-3:])].append(x[:-3])
    else:
        # if x not in d.keys():
        #     d[int(x)] = ['0']
        #     continue
        d[int(x)].append('0')

s = sorted(d.keys())
# print(d)
for q in s:
    # print(q,len(d[q]))
    p-= len(d[q])
    if p<=0:
        if d[q][p+len(d[q])-1]==0:
            print(d[q])
            break
        # print(d[q][p+len(d[q])-1])
        print(d[q][p+len(d[q])-1]+str(q))
        break
