#!/usr/bin/python
# File Name: run.py
# Author: Changsheng Zhang
# mail: zhangcsxx@gmail.com

#########################################################################

import os
import time

for ii in xrange(1000):

    print "begin run\n"
    os.system("scrapy crawl stock")

    print "done, begin sleep"
    a = 3600*24
    time.sleep(a)
