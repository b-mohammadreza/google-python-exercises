#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

def get_special_paths(input_dir):
  special_paths = []
  file_names = os.listdir(input_dir)

  for file in file_names:
    #print(f'get_special_paths(): file to examine: {file}')
    if re.search(r'__\w+__', file):
      special_paths.append(os.path.abspath(os.path.join(input_dir, file)))

  return special_paths


# copy src files to dest
def copy_to(file_paths, to_dir_path):
  if not os.path.exists(to_dir_path):
    os.makedirs(to_dir_path)

  file_names = []
  for path in file_paths:
    file_name = os.path.basename(path)

    if file_name not in file_names:
      shutil.copy(path, to_dir_path)
    else:
      print(f'Error: Duplcate file name: {file_name}')

    file_names.append(file_name)

  return


def zip_to(paths, zip_path):
  cmd = f'zip -j {zip_path} '
  for path in paths:
    cmd += f'{path} '

  print(f'Command to run: {cmd}', end='')
  (status, output) = subprocess.getstatusoutput(cmd)

  if status:
    sys.stderr.write(f'{output}\n')
    sys.exit(status)
  return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)

  special_paths = []
  for dir in args:
    special_paths.extend(get_special_paths(input_dir=dir))

  if not todir:
    for path in special_paths:
        print(path)
  else:
    copy_to(special_paths, todir)


  if tozip:
    zip_to(paths=special_paths, zip_path=tozip)

  
if __name__ == "__main__":
  main()
