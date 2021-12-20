import unittest
from mydict  import Dict

class TestDict(unittest.TestCase):

    def setUp(self):
        print('setup')
    
    def tearDown(self):
        print('tearDown')

    def test_init(self):
        d = Dict(a = 1,b = 'test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    
    def test_key(self):
        d =Dict()
        d['key'] = 'value'
        self.assertTrue(isinstance(d,dict))
    
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue(d.key,'value')
        self.assertEqual(d['key'],'value')

#编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

#以test开头的方法就是测试方法，
# 不以test开头的方法不被认为是测试方法，测试的时候不会被执行。


#一旦编写好单元测试，
# 我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()

#这是推荐的做法，因为这样可以一次批量运行很多单元测试，
# 并且，有很多工具可以自动来运行这些单元测试。

#可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
# 这两个方法会分别在每调用一个测试方法的前后分别被执行。
