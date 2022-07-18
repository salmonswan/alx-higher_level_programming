#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            _div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            _div = 0
        except TypeError:
            print("wrong type")
            _div = 0
        except IndexError:
            print("out of range")
            _div = 0
        finally:
            new.append(_div)
    return (new)
