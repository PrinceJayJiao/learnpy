#错误处理
#在程序运行的过程中，我们可以事先约定但会一个错误码，
# 这样可以知道是否出错，哪里出错，出了什么错
#但是错误码容易和我们正常工作产生的返回码所混淆，我们必须要用大量的代码来判断错误

#try.... except... finally...错误处理机制
import logging
from io import BytesIO, StringIO
import os
import pickle
import json

try:
    #your code here
    pass
except ZeroDivisionError as e:
    # if error appears, jump here
    pass
except ValueError as e:
    #可以有多个错误处理部分
    pass
else:
    #如果你代码没错，执行完就会到这
    pass
finally:
    #optional 最终会到这（如果有的话）
    pass

#多层调用的时候，不用在每个可能出错的地方都捕获，只需要在合适的时候捕获就行了

# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
#调用栈
#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，
# 然后程序退出
#logging模块可以很容易的记录错误信息
def fn1():
    try:
        #your code here
        pass
    except Exception as e:
        logging.exception(e)
#同样是出错，但程序打印完错误信息后会继续执行，并正常退出：

#抛出错误
#如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
#raise 可以抛出错误
def fn2():
    try:
        #your code here
        pass
    except ValueError as e:
        print('value error')
        raise
        raise ValueError('input error')
        #两种抛出都可以，意思是你可以原封不动抛出当前的错误，也可以抛出其他错误
#我们虽然已经捕获到错误并且输出了，但是我们还是抛出了这个错误，就像我们处理不了的东西
#交给老板处理一样


#debug
#第一种，输出调试，暴力调试，直接打印可能有问题的变量看看

#第二种assert expressions

#第三种 logging
#这就是logging,它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
#当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

#如何制定输出级别？
#import logging
#logging.basicConfig(level=logging.INFO)

#logging的另一个好处是通过简单的配置，
# 一条语句可以同时输出到不同的地方，比如console和文件

#4 pdb python调试器
# command : python -m pdb xxx.py
#以参数-m pdb启动后，pdb定位到下一步要执行的代码。输入命令l来查看代码：
#输入命令n可以单步执行代码
#p 变量名 可以查看变量
#输入命令q结束调试，退出程序：

#pdb.set_trace()
#这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，
# 然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：

#ide调试
#不过最后发现还是logging np


#测试
#测试驱动开发TDD(Test-driven development)

#单元测试是用来对一个模块，一个函数或者一个类来进行正确性校验的测试性工作
#example code 在test文件夹下


#文档测试
#当我们编写注释时，如果写上这样的注释：
def myabs(n):
    '''
    function to get absolute value of number

    example:
    >>> abs(1)
    1
    >>>abs(-1)
    1
    >>>abs(0)
    0
    '''
    return n if n>0 else (-n)
    #无疑更明确地告诉函数的调用者该函数的期望输入和输出。
#python 内置的文档测试，(doctest) 模块可以直接提取注释中的代码并且进行测试。




#io
#读文件
f = open('path/to/file','r')#r表示只读方式打开文件
#文件不存在时会抛出IOError
f.read()#一次读取全部内容
f.close()#关闭资源


#with 自动关闭
with open('path/to/file','r') as f:
    print(f.read())
    f.read(1024)#读取1024字节
    f.readline()#读一行
    f.readlines()#读取全部行，返回list

#二进制文件，rb模式打开
jpg = open('path/to/img','rb')

#指定字符编码读取
f = open('path','r',encoding = 'utf-8')
#忽略文件中部分错误编码
f =open ('path','r',encoding= 'utf-8',errors= 'ignore')

#写文件
f = open('path','w')
#二进制写
f = open('path','wb')
#追加
f = open('path','a') #append

f = StringIO()
f.write('hello')
f.write('')
print(f.getvalue())#获得写入的str
#读取
f = StringIO('hello')#用str初始化stringIO
f.read()

#BytesIO
#写
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
#读
f = BytesIO(b'\xe4\xb8\xad\xe6')
f.read()

#操作文件和目录
#python 内置的os模块可以调用操作系统接口
os.name #操作系统类型
os.uname()#操作系统详细信息
os.environ#操作系统环境变量
key = 'path'
os.environ.get(key)#获取某个环境变量的值
os.path.abspath('.')#查看当前目录的绝对路径
os.path.join('path/dir1','dir2') #path/dir1/dir2
os.path.spli('path')#拆分为路径和文件名
#这样在不同的操作系统下返回不同的路径分隔符
#不要求文件存在，只是对字符串操作而已

os.mkdir('path/to/dir')#创建，删除文件夹
os.rmdir('path/to/dir')
os.rename('test.txt','test.dat')#对文件重命名
os.remove('test.dat')#删

#列出当前目录下所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]
#列出所有py
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


#Python提供了pickle模块来实现序列化。
d = dict(name = 'jay',age = 19,score =99)
f = open('path','wb')
pickle.dumps(d)#返回一个字符序列
pickle.dump(d,f)#序列化后写到文件里面
f.close()
#反序列化
f = open('path','rb')
d = pickle.load(f)
f.close()


#json
#python 内置的json模块提供了python对象到json的转换
#import json
d = dict(name = 'jay' ,age = 18,score = 100)
str = json.dumps(d)#序列化为json
json.loads(str)#反序列化

#对象转化为json需要实现转换函数,先把它转化为dict
class Class1(object):
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

def s2j(stu):
    return{
        'name': stu.name,
        'age': stu.age
    }
c1 =Class1()
json.dumps(c1,default= s2j)
#同理我们需要写反转化函数
def dict2c1(d):
    return Class1(d['name'],d['age'])

#如果下次遇到一个新类，我们都要这么做实在太麻烦了
#因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class。
class Class2(object):
    pass

c2 = Class2()
json.dumps(c2,default= lambda obj:obj.__dict__)
