#!/usr/bin/python

import time

def report_letter(c):
  print(chr(ord('z') - c))

count = 10
#! results in a en endless loop. why?
while count > 0:
  # in python --count means -(-(count))
  report_letter(count)
  count -= 1