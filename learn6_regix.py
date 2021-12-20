#正则表达式

## 1匹配字符串
### 直接给出字符就是精确匹配
# \d匹配一个数字
# \w匹配一个数字或者字母
# \s 匹配一个空格
# .可以匹配任意字符
# *表示任意个字符
# +表示至少一个字符
# ?表示0或1个字符
# {n}表示n个字符
# {n,m}表示n到m个字符
#eg
'\d{3}\s+\d{3,8}'
#3个数字，至少一个空格,3到8个数字


#要做更精确的匹配，还可以用[]表示范围
'[0-9a-zA-z\_]' #可以匹配一个数字、字母、下划线
# a|b 匹配a或者b
#^表示行的开头，^\d表示，必须以数字开头
#$表示行的结束， \d$表示必须以数字结束


import re
from datetime import datetime, timedelta, timezone
from collections import deque, namedtuple


s = r'abc\-001'
m = re.match(r'^\d{3}\-\d{3,8}$','010-1234')
#匹配成功则返回一个match对象，匹配失败则返回none

if m:
    print('ok')
else:
    print('failed')

#切分字符串
re.split(r'[\s\,\;]+','a  c b d   x,t;  p')
#切开中间以空格逗号分号分隔的字符


#分组
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。
# 用()表示的就是要提取的分组（Group）。比如：
'^(\d{3})-(\d{3,8})$'
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
m.group(0)#010-12345
m.group(1)#010
m.group(2)#12345
#注意到group(0)永远是原始字符串

#贪婪匹配
#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：
re.match(r'^(\d+)(0*)$', '102300').groups()#('102300', '')
#前面的\d+把所有的0全部匹配了，0*就匹配不到任何东西
#必须让\d+采用非贪婪匹配（也就是尽可能少匹配），
# 才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
re.match(r'^(\d+?)(0*)','102300').groups()#('1023','00)

#正则表达式需要被编译，所以我们写好一个正则表达式最好先编译，
# 然后用一个变量引用返回的结果，就不用重复编译
# 编译后生成Regular Expression对象，
# 由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
re_teltphone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_teltphone.match("010-12345").groups()
re_teltphone.match('000-54321').groups()


#常用的内建模块
#获取当前的日期和时间
# from datatime import datetime
now = datetime.now()
print(now)

dt = datetime(2015,4,19,12,20,20,100)#创建指定时刻


#timestamp 时间戳 相对于1970年1月1日的秒数 浮点数，整数位表示秒

tt = dt.timestamp()#把dt转化为时间戳

datetime.fromtimestamp(tt)#把时间戳转化为datetime 本地时区
datetime.utcfromtimestamp(tt)# utc标准时区

#str转datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')

#datetime 转str
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))

#时区加减 #引入timedelta
now = datetime.now()
now+timedelta(hours=10)
now + timedelta(days=1)

#本地时间转utc时间
tz_utc_8 = timezone(timedelta(hours=8))#创建时区utf-8


#collections

#namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
p.x # 1
p.y # 2

#deque
#双向列表，支持两端的插入删除
dq = deque(['a','b','c'])
dq.append('x')
dq.appendleft('y')
dq.pop()
dq.popleft()
#后面的自己看





