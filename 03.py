#!/usr/bin/python

import fnmatch
import os
import subprocess
import tempfile

with tempfile.NamedTemporaryFile(suffix='.py', dir='.') as tmp:
  print('Tempfile name %s' % tmp.name)
  tmp.write('nonsense')
  print('File %s exists: %s' % (tmp.name, os.path.exists(tmp.name)))
print('File %s exists: %s' % (tmp.name, os.path.exists(tmp.name)))

print('*'*10 + ' python native')
for file in os.listdir('.'):
  if fnmatch.fnmatch(file, '*.py'):
    print(file)

print('*'*10 + ' system call')   
#! raises an exception
# fix the call so it displays the same content (different order is ok) as the native python code
print(subprocess.check_output('ls *.py', shell=True))

