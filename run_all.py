# -*- coding: utf-8 -*-
import unittest
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./")

f = open("report.html", 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="福建公共服务接口测试",description="包括厦门,福州,泉州,宁德",tester="linsp").run(suite)
f.close()