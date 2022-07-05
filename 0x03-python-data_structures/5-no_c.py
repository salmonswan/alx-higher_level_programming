#!/usr/bin/python3
def no_c(my_string):
    str_p = ""
    for i in my_string:
        if i not in ['c', 'C']:
            str_p += i
    return (str_p)
