#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuples_1, tuples_2 = [tuple_a, tuple_b], []
    for tuple in tuples_1:
        if len(tuple) < 2:
            while len(tuple) < 2:
                tuple = (*tuple, 0)
        else:
            tuple = tuple[0:2]
        tuples_2.append(tuple)
    tup_sum = (
        tuples_2[0][0] + tuples_2[1][0],
        tuples_2[0][1] + tuples_2[1][1]
        )
    return (tup_sum)
