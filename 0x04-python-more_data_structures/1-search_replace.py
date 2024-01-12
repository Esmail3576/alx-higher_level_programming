#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [i for i in my_list]
    for i in new_list:
        if i == search:
            new_list[i-1] = replace
    return new_list
