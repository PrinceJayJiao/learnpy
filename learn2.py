#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'
__author__ = 'jay'

from os import name
import sys
from types import MethodType
from enum import Enum, unique

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello')
    elif len(args) == 2:
        print("hello %s" % args[1])
    else:
        print('too many args')

if __name__ == '__main__':
    test()

#class
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

bart = Student("jay",18)
#和普通的函数相比，在类中定义的函数只有一点不同，
# 就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。

#数据封装
class Man(object):
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def print_age(self):
        print("he is %d years old!" %self.age)

##访问限制
#如果想要内部属性不被外部访问，可以在名称前面加上两个下划线__
#python中 如果变量名以__开头，就变成了一个私有变量，只有外部可以访问，内部不可以访问

class Woman(object):
    def __init__(self,name,age) -> None:
        self.__name = name
        self.__age = age
    def print_name(self):
        print("her name is %s" % self.name)
    def get_name(self):
        return self.__name
    def set_name(self,name):
         self.__name = name

#双下划线开头和结尾的不是私有变量，可以在外部访问
#单下划线开头的，外部可以访问，但是请尽量不要随便访问


##继承和多态
class Person(object):
    def born(self):
        print("the person is born")


class Man(Person):
    def born(self):
        print("he is born!")

class Woman(Person):
    def born(self):
        print("she is born!")

m = Man()

def born10(person):
    n = 10
    while n>0:
        person.born()
        n = n-1

born10(m)

#对于静态语言（例如Java）来说，
# 如果需要传入person类型，则传入的对象必须是person类型或者它的子类，
# 否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入person类型。
# 我们只需要保证传入的对象有一个run()方法就可以了：
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
# 一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。


#获取对象信息

#type()
type(123)
type(abs) #abs为函数
#判断函数
#import types
#def fn():
#   pass
#type(fn) == types.FunctionType
#type(abs) == types.BuiltinFunctionType
#type((x for xin range(10))) == types.GeneratorType

#isinstance()
# 继承 object man student high school student
#可以用isinstance 来判断
isinstance([1,2,3],(list,tuple)) # 判断是不是list或者tuple中的一种
#能用type()判断的基本类型也可以用isinstance()判断
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

#dir()
#获得一个对象的所有属性和方法 返回一个字符串list
#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObj(object):
    def __init__(self) -> None:
        self.x = 100
    def power(self):
        return self.x*self.x

obj = MyObj()

hasattr(obj,'x') #判断obj中是否含有属性x
setattr(obj,'y',19) #在obj中新增一个属性y并且赋初值19
getattr(obj,'y') #获取属性y
#如果试图获取不存在的属性，会抛出AttributeError的错误
#可以传入一个default参数，如果属性不存在，就返回默认值
getattr(obj,"notexist",404) #如果属性不存在就返回默认值

#这三个函数不仅可以获得属性，也可以获得方法
fn = getattr(obj,'power')
fn()
obj.power()
#上面两个函数等效

class Test(object):
    name = 'Test'

t = Test()
print(t.name)#Test
print(Test.name)#Test
t.name = "jay"
print(t.name)#jay
print(Test.name)#Test
del t.name
print(t.name)#Test
print(Test.name)#Test


#使用__slots__
#定义一个class，创建一个实例后，我们可以为实例绑定任何属性和方法
class Test2(object):
    pass

s = Test2()
s.name = 'tomdd'

def method1(self,name):
    self.name = name

s.set_name = MethodType(method1,s)#给实例绑定一个方法
#但是这个方法仅仅对这一个实例起作用，对其他实例不起作用
#可以给类绑定方法
Test2.set_name = method1#给类绑定方法
#绑定之后，所有实例都可以调用

#怎么样限制实例的属性，我们不想要被人向我们的类里面随随便便加上乱七八糟的属性
#__slot__
class Test3(object):
    __slot__ = ('name','age') #tuple 定义允许绑定的属性名称

t3 = Test3()
t.name = 'jay'#ok
t.score = '59' #error attributeerror
#__slot__定义的属性仅仅对当前类的实例起作用，对它的子类不起作用
#如果想起作用，在子类也绑定就行了

#@property
class Test4(object):
    def __init__(self,age) -> None:
        super().__init__()
        self._age = age

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return self._age

t4 = Test4(10)
t4.birth = 1000
t4.birth
t4.age
#简化了getter setter书写
#可以设置只读，只写，可读可写属性
#要特别注意：属性的方法名不要和实例变量重名。self._birth 方法名birth
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，
# 同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


#多重继承
#通过多重继承，一个子类就可以同时获得多个父类的所有功能。
#有点类似于java接口的意思？（不等于！！！java只能继承一个类，可以实现多个接口）
#一个dog可以继承自mammal(哺乳动物) 和runnable(可以奔跑的)

#mixIn（设计模式）
#为了更好的看出来继承关系，我们可以把mammal保留不变，而把runnable写成runnableMixIn
#可以让他有多个MixIn
class Mammal(object):
    pass
class RunnableMinxIn(object):
    pass
class CarnivorousMixIn(object):#食肉动物
    pass

class Dog(Mammal,RunnableMinxIn,CarnivorousMixIn):
    pass

#MixIn的目的就是给一个类增加多个功能，
# 这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
#有点java接口那味了


#定制类
#形如__xxx__ 的变量或者函数名，一般都是由特殊用途的
#__slot__  
# __len__为了class能被len()所作用
#__str__ 在打印对象的时候，可以自定义打印出来的内容
class Test5(object):
    def __init__(self,name) -> None:
        self.name = name
print(Test5("jay"))

class Test6(object):
    def __init__(self,name) -> None:
        self.name = name
    def __str__(self): # 在程序输出对象时调用
        return "test object name %s " %self.name
    __repr__ = __str__#在程序调用Test5('testname)时作为返回值
print(Test5("jay"))

#要想实现forin循环，就必须实现一个__iter__方法
#__getitem__()可以实现索引取对象
class Fib(object):
    def __init__(self) -> None:
        super().__init__()
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a >100000:
            raise StopIteration()
        return self.a
    def __getitem__(self,n):
        a,b = 1, 1
        for x in range(n):
            a,b = b, a+b
        return a

for i in Fib():
    print(i)

print(Fib()[5])
#实现切片需要在__getitem__中进行判断
def __getitem__(self,n):
    if isinstance(n,int):
        a,b = 1,1
        for x in range(n):
            a,b = b, a+b
        return a
    if isinstance(n,slice):
        start = n.start
        end = n.end
        if start is None:
            start = 0
        a,b = 1, 1
        L = []
        for x in range(end):
            if x>= start:
                L.append(a)
            a, b = b, a+b
        return L
Fib.__getitem__ = __getitem__
#还可以添加参数step...

class Test7(object):
    def __init__(self) -> None:
        self.name = 'mike'
    
    def __getattr__(self,attr):
        if attr =='score':
            return 99
t7 = Test7()
t7.score#虽然这个属性不存在，但是可以利用getattr返回属性
#也可以返回函数
def __getattr__(self,attr):
    if attr == 'score':
        return lambda:25
Test7.__getattr__ = __getattr__
t7.score()
#在找不到属性的时候才会调用__getattr__, 对于已有的属性不会
#如果方法中没有对应的属性响应，则默认返回None
#但是我们最好返回一个错误
def __getattr__(self,attr):
    if attr == 'age':
        return 19
    raise AttributeError('\'student\' has no attribute %s' % attr)

#这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
#这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
#后面他举得例子我看不懂...麻了
# __call__

#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
class Test8(object):
    def __init__(self) -> None:
        self.name = name
    def __call__(self):
        print('my name is %s' % self.name)

t8 = Test8('michael')
t8()
#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
# 所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。


#枚举类
month = Enum('month',('jan','feb','mar'))#etc后面不写了
#就是一个常量
for name, member in month.__members__.items():
    print(name, '=>', member, ',',member.value)

#value 是自动赋给成员的int常量，默认从1开始
#如果要更精确的控制枚举类型，可以从enum派生出自定义类：

@unique#帮助检查保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Teu = 2
#..太多了，懒得写
#访问方法
Weekday.Mon #WeekDay.Mon
Weekday['Tue'] #Weekday.Tue
Weekday.Mon.value # 1
Weekday(1) #WeekDay.Mon


#使用元类
#动态语言和静态语言最大的不同就是函数和类的定义，
# 不是编译时定义的，而是运行时动态创建的。
#type()函数可以查看一个类型或变量的类型
# ，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
class Hello(object):
    pass
h = Hello()
#我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
#type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self,name = 'world'):
    print('hello, %s ' % name)

Hello = type('hello',(object,),dict(hello = fn))#创建hello class

#要创建一个class对象，type()函数依次传入3个参数：

#1 class的名称；
#2 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3 class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

#通过type创建的类和直接写class是完全一样的。

#我不想让这一个文件太大，就写到这吧，下一个文件见
