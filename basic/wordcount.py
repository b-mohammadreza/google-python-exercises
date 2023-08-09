#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
from operator import itemgetter


def read_file_create_dict(file_name) -> dict:
  result_dict = {}

  with open(file_name, 'rt', encoding='utf-8') as f:
    for line in f:
      for word in line.split():
        word = word.lower()
        if word in result_dict:
          result_dict[word] += 1
        else:
          result_dict[word] = 1

  f.close()
  return result_dict






def sort_dict_by_word(keys : list) -> list:
  return sorted(keys) 





def sort_dict_by_count(items : list) -> list:
  return sorted(items, key=itemgetter(1), reverse=True)





def print_words(file_name):
  dict_1 = read_file_create_dict(file_name=file_name)
  sorted_keys = sort_dict_by_word(dict_1.keys())

  for key in sorted_keys:
    print(f'key: {key:25}, value: {dict_1[key]:3}')
  return







def print_top(file_name):
  dict_1 = read_file_create_dict(file_name=file_name)
  sorted_items = sort_dict_by_count(dict_1.items())

  range_max = 20
  if len(sorted_items) < range_max:
    range_max = len(sorted_items)

  for index in range(range_max):
    print(f'{index+1:3}  >>  key: {sorted_items[index][0]:25}, value: {sorted_items[index][1]:5}')

  return

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
