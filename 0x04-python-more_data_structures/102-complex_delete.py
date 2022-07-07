#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values = list(map((lambda x: x[1]), a_dictionary.items()))
    if value not in values:
        pass
    else:
        dict_list = []
        for i, j in a_dictionary.items():
            if j != value:
                dict_list.append((i, j))
        a_dictionary = dict(dict_list)
    return (a_dictionary)
