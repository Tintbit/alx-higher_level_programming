#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list): # other solution if idx<0 or len(my_list)<=idx return None
        return None
    else:
        return my_list[idx]
