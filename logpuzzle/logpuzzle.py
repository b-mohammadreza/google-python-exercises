#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def custom_key(url):
  pattern_match = re.search(r'-\w*-(\w*).jpg', url)

  if pattern_match:
    return pattern_match.group(1)

  return url


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""

  name_match = re.search(r'_(\w+\.\w+\.\w+)', filename)
  if name_match:
    host_name = name_match.group(1)
  else:
    print('Error! host name not found')
    sys.exit(1)

  host_name = 'http://'+host_name
  url_list = []

  with open(file=filename, mode='rt', encoding='utf-8') as log_file:
    for line in log_file:
      baseurl_match = re.search(r'GET\s(\S*[Pp][Uu][Zz][Zz][Ll][Ee]\S*)\sHTTP', line)

      if baseurl_match:
        base_url = baseurl_match.group(1)

        url = host_name+base_url
        if url not in url_list:
          url_list.append(url)

  log_file.close()

  url_list = sorted(url_list, key=custom_key)

  return url_list

  

def download_images(img_urls : list, dest_dir : str):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

  if dest_dir.find('/', -1, len(dest_dir)) == -1:
    dest_dir += '/'

  for index in range(len(img_urls)):
    if index % 3 == 0:
      postfix = '.  '
    elif index % 3 == 1:
      postfix = ' . '
    else:
      postfix = '  .'
    print(f'Retrieving{postfix}', end='\r')

    file_name = f'{dest_dir}img{index}'
    urllib.request.urlretrieve(url=img_urls[index], filename=file_name)

  print('            ', end='\r')

  with open(file=f'{dest_dir}index.html', mode='wt', encoding='utf-8') as index_file:
    index_file.write('<html>\n')
    index_file.write('<body>\n')

    for index in range(len(img_urls)):
      index_file.write(f'<img src="img{index}">')

    index_file.write('\n')
    index_file.write('</body>\n')
    index_file.write('</html>')
  index_file.close()

  return


def main():
  args = sys.argv[1:]

  if not args:
    print ('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print ('\n'.join(img_urls))

if __name__ == '__main__':
  main()
