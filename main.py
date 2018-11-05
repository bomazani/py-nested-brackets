#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.

There should be a blank line in between description above, and this
more detailed description. In this section you should put any caveats, 
environment variable expectations, gotchas, and other notes about running
the program.  Author tag (below) helps instructors keep track of who 
wrote what, when grading.
"""
__author__ = "bomazani"

# Imports go at the top of your file, after the module docstring.
# One module per import line. These are for example only.

import sys
from math import pi

# This statement will run once at module import.
print("Executing module import, name is {}".format(__name__))


def check_brackets(string):
    mystring = string.replace(' ', '_')
    mystring = mystring.replace('(*', '$')
    mystring = mystring.replace('*)', '%')
    open_list = []
    open_count = 0
    close_count = 0
    close_list = []
    popped_item = []
    open_brackets = ['(', '{', '[', '<', '$']
    close_brackets = [')', '}', ']', '>', '%']
    for i in enumerate(mystring, 1):
        if i[1] in open_brackets:
            open_list.append(i)
            open_count += 1
        if i[1] in close_brackets:
            close_count += 1
            close_list.append(i)
            if close_count > open_count:
                return
            if i[1] == close_brackets[0] and open_list[-1][1] == open_brackets[0]:
                popped_item.append(open_list.pop())
            elif i[1] == close_brackets[1] and open_list[-1][1] == open_brackets[1]:
                popped_item.append(open_list.pop())
            elif i[1] == close_brackets[2] and open_list[-1][1] == open_brackets[2]:
                popped_item.append(open_list.pop())
            elif i[1] == close_brackets[3] and open_list[-1][1] == open_brackets[3]:
                popped_item.append(open_list.pop())
            elif i[1] == close_brackets[4] and open_list[-1][1] == open_brackets[4]:
                popped_item.append(open_list.pop())
            else:
                print('No', i[0])
                return

    if open_count == close_count:
        print 'Yes'
    elif open_count > close_count:
        print 'No', len(mystring) + 1
    else:
        print ('No', popped_item[0][0])
    return


check_brackets('(*a++(*)')
check_brackets('(*a{+}*)')
check_brackets('    <************)>')
check_brackets('    ()(***)(**)')
check_brackets('   ()(***)(*)')
check_brackets('({{}{}}[{(){}[]}')
check_brackets('   ([))')
check_brackets(' ()(**)')
check_brackets('    ()*')
check_brackets(' aaaaaaa')
check_brackets('    aaa(aaaa')
check_brackets(' *******')

if __name__ == '__main__':
    """Docstring goes here"""
    print("Command line arguments: {}".format(sys.argv))
    # Invoke standalone main() with cmdline argument list.
    # Program should return status==0 if no errors.
    status = main(sys.argv)
    # return status code to OS.
    sys.exit(status)


# This statement will run once at module import.
print("Executing module import, name is {}".format(__name__))
