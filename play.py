# -*- coding: utf-8 -*-

import pickle,time

# 从 文件中 读取并恢复 对象
l1 = pickle.load(open("cc", "r"))
 
#print l1
import win32api as w

#回放是 逆过程
for i in l1:
    time.sleep(0.01)
    w.SetCursorPos(i)





