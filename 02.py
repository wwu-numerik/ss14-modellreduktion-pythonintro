#!/usr/bin/python

from timer import Timer

rmax = int(2e7)
with Timer('list code'):
  for _ in range(rmax):
    _ = 0
with Timer('iterator code'):
  #! change to iterable range 
  for _ in xrange(rmax):
    _ = 0
# time needed after the change should roughly be halved




