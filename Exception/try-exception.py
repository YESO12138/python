# -*- coding:utf-8 -*-
#使用try -except 形式捕获异常
try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError as e:
    print(u"捕获到异常",e)
finally:
    print("hello world")