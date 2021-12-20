from collections.abc import Iterable
import os
import functools


# list
from typing import KeysView


list = [1,2,"tom",3,False,[1,2]]
print(list[5])
len(list)

#tuple
tuple = (1,2,'jay')
# 一旦初始化就不可以修改

#定义只有一个元素的tuple
t1 = (1)#错误
t2 = (1,) #正确

#条件判断
age = 19
if age>18: #记得加冒号
    pass #pass为占位符号，表示什么也不做
elif age>10:
    pass # else if
else:
    pass #else


#input
birth = input("info str") #读取输入到birth, info str 为提示性字符

#循环
list = [1,2,3]
for item in list:
    print(item)

#range
list(range(10)) #range生成一个整数序列，通过list转化为list 生成为0-9

#dict
dict = {'Michael':40,'jay':90,'tracy':100}
print(dict['Michael'])   #相当于键值对类型

if "jay" in dict:
    pass #首先判断键jay在列表中,防止出错
#get
dict.get("jay") #同上，可避免出错
dict.get("jay",-1) #指定默认值

#set
#以list为输入创建set，重复元素在set中自动被过滤
s = set([1,1,2,2,2,3])
s2 = set([1,2,3]) #s1和s2中的内容是一模一样的
s.add(4)#添加key到set，可以重复添加，但是不会有任何效果
s.remove(2) #从set中删除key

#两个set可以取交集并集，就像数学意义上的集合
#set和dict都不能放入可变对象


#函数

#内置函数
#abs
abs(100) #取绝对值
#max
max(10,2,3,100) #取最大值
#数据类型转换
int('100') #str转int
str(10.22) #int转str
bool(0)
bool(1)

a = abs #函数起别名
#定义函数 def

def my_abs(x):
    if x>0:
        return x
    else:
        return -x
#自定义函数abs

#返回多个值的函数
def twoRet():
    return 1, 2
x, y = twoRet()
#返回值其实是一个tuple,两个变量可以接收一个tuple，按位置赋给相应的值

#参数
#位置参数
def power(x):
    return x*x
#x就是一个位置参数
#默认参数
def powern(x,n = 2):
    s = 1
    while n > 0:
        s = s*x
        n-n-1
    return s
#n就是一个默认参数
#必选参数在前，默认参数在后
#默认参数必须指向不变对象！！！！！！

#可变参数
def calc(*nums):
    sum=0
    for num in nums:
        sum = sum +num*num
    return sum
#调用
calc(1,2,3)
nums = [1,2,3,4]
calc(*nums) #在list或者tuple前加一个*就可以传到可变参数的函数里面

#关键字参数
def person(name,age,**kw):
    print(name,age,kw)

#调用时可以只传入必选参数
#也可以传入任意的关键字参数

extra = {'city':'beijing','job':'engineer'}
person('jack',24,**extra)

#命名关键字参数
def person1(name,age,* ,city,job):
    print(name,age,city,job)
# *后面的为命名关键字参数


#递归函数

def fact(n):
    if n == 1:
        return 1
    return n* fact(n-1)

#切片 用来取list或者tuple中的部分元素
L= ['jay','tom','khan']
[L[0],L[1],L[2]] # common ways

r = []
for i in range(3):
    r.append(L[i]) #higher ways

#切片
L[0:3] #左闭右开
L[:3] #第一个索引为0的时候可以省略
L[-2:] #倒数切片，最后一个索引是-1

L = list(range(100))
#前十个数，每两个取一个
L[:10:2]
#所有数，每五个取一个
L[::5]
#复制一个list
L[:]
#字符串和tuple也可以看作特殊的list，所以也可以切片


#迭代
d = {1:'a',2:'b',3:'c',4:'d'}
for key in d:
    print(key) #迭代key
for value in d.values():
    print(value) #迭代value
for k, v in d.items():
    print(k,v)#同时迭代kv
#str也可以被迭代

#利用collections.abc的Ierable判断对象是否可以被迭代
isinstance('abc',Iterable)
#enumerate可以把list变成索引-元素对，在for中可以迭代索引和元素本身
for i,value in enumerate(['a','b','c']):
    print(i,value)


#列表生成式
for x in range(1,11):
    L.append(x*x) #common ways
[x*x for x in range(100)] #列表生成式
[x*x for x in range(100) if x%2 == 0] #0-99中偶数的平方
[m+n for m in 'abc' for n in 'xyz']#两层循环生成全排列
[d for d in os.listdir('C:')] #列出c盘下所有的文件和目录
[k+','+'v' for k,v in d.items()] #两个变量生成list

#在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
[x for x in range(100) if x%2 == 0] #这个if是筛选条件，后面不能跟else
[x if x%2 ==0 else -x for x in  range(100)] #这个if是条件表达式，可以有else


#生成器
L = [x*x for x in range(10)]
g = (x*x for x in range (10)) #生成器 generater
#可以直接打印出list中的元素
#利用next()函数可以获得generater的下一个返回值
#也可以通过迭代把他打印出来
#如果一个函数中含有yield关键字，则就是一个generate函数，返回值为generator


#迭代器
#可以利用Iterable 判断是不是可迭代对象（Iterable对象）
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#可以利用isinstance判断是否为Iterator对象
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：


#高阶函数

#1变量可以指向函数
#2函数名也是变量
#接收另一个函数为参数的函数为高阶函数

#map/reduce
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x
l= map(f,[1,2,3])


#reduce
#   reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#filter()用于过滤序列


## 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
## filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#lambda
#匿名函数
f = lambda x: x*x#这个是下面函数的匿名函数
def f(x):
    return x*x
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#装饰器
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2015-3-25')

#偏函数
int2 = functools.partial(int,base = 2)
int2('10000')

