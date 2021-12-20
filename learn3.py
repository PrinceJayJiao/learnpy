#书接上回
#metaclass
#可以使用type()创建类
#控制类的创建行为，可以使用metaclass(直译为 元类)
#啥jb玩意是元类
#先创建metaclass，由metaclass创建我们的类
#再由类创建出我们的实例


##metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
# 正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
##好，真不错啊，拜拜
#。。。。。


#定义ListMetaclass，
# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self, value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass = ListMetaclass):
    pass

##暂时写到这，下次一定