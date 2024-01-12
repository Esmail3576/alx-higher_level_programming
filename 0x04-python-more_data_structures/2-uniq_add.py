#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = list(set(my_list))
    result = 0
    for i in unique_list:
        result = result + unique_list[i-1]
    return result
