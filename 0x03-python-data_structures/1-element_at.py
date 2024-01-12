#!/usr/bin/python3
def element_at(my_list, idx):
	i = 0
	if idx < 0 || idx > len(my_list):
	return
	while i < len(my_list):
		if i == idx:
		return my_list(i)
		i = i + 1
