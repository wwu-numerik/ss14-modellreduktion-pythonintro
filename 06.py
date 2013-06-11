#!/usr/bin/python

def foo(bar=[]):
  bar.append('o')
  return bar

#! fix the function so all calls return the same
print(foo())
print(foo())
print(foo())
print(foo([]))
