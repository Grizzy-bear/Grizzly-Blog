import unittest
import xmlrunner

# 导入模块

def fun(x):
    return x+1

class Mytest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
        print("chengong")

if __name__ == "__main__":
    unittest.main()

# suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Mytest))


