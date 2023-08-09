#!/usr/bin/env python

import sys

def main():
    #print('hello there', sys.argv[1])
    print(repeat('yo',True))
    str_demo()

def repeat(s, exclaim):
    result = s+s+s
    #result = s*3

    if exclaim:
        result += '!!!'
    
    return result

def str_demo():
    sample_str = 'Mohammadreza'
    print(sample_str[-5:-2])
    print(sample_str[:-2])
    print(sample_str[1:6])

    # formatted str
    value = 2.65889
    print(f'formatted value: {value:.2f}')
    print(f'formatted value: {value}')
    car = {'tires':4, 'doors':2}
    print(f'car: {car}')

    # prinf style formating
    text = (
    "%d little pigs come out,"
    " or I'll %s, and I'll %s,"
    " and I'll blow your %s down."
    % (3, 'huff', 'puff', 'house'))

    print(text)

    return

if __name__ == '__main__':
    main()