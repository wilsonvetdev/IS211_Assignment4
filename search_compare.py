
import random 

def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list 

def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

def ordered_sequential_search(a_list, item):
    pos = 0
    found = False 
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item: 
            found = True 
        else:
            if a_list[pos] > item:
                stop = True 
            else: 
                pos = pos + 1
    
    return found




print(get_me_random_list(10))
sequential_search()