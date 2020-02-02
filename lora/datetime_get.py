#!/usr/bin/python

import datetime
import time

for i in range(1,100) :
  print str(datetime.datetime.utcnow().time())
  time.sleep(1)
