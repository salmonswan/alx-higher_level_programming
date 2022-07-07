#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        pass
    else:
        dict_list = []
        for i, j in a_dictionary.items():
            if j != value:
                dict_list.append((i, j))
        a_dictionary = dict(dict_list)
    return (a_dictionary)
