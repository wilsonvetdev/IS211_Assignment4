
import random 
import time

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

def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False 

    while first <= last and not found: 
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True 
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1 
            else: 
                first = midpoint + 1
    
    return found 

def binary_search_recursive(a_list, item): 
    if len(a_list) == 0: 
        return False
    else: 
        midpoint = len(a_list) // 2 

    if a_list[midpoint] == item: 
        return True 
    else: 
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else: 
            return binary_search_recursive(a_list[midpoint + 1:], item)

if __name__ == "__main__":

    random.seed(100)

    list_sizes = [500, 1000, 5000]

    for list_size in list_sizes:
        total_time = 0
        for i in range(100):

            mylist = get_me_random_list(list_size)
            start = time.time()
            # search function to test 
            sequential_search(mylist, -1)
            end = time.time()
            sort_time = end - start
            total_time += sort_time
        
        avg_time = total_time / 100
        print(f"Avg time to sort a list of {list_size} using sequential search: {avg_time:0.08f} seconds")

    for list_size in list_sizes:
        total_time = 0
        for i in range(100):

            mylist = get_me_random_list(list_size)
            mylist.sort()
            start = time.time()
            # search function to test 
            ordered_sequential_search(mylist, -1)
            end = time.time()
            sort_time = end - start
            total_time += sort_time
        
        avg_time = total_time / 100
        print(f"Avg time to sort a list of {list_size} using ordered sequential search: {avg_time:0.08f} seconds")

    for list_size in list_sizes:
        total_time = 0
        for i in range(100):

            mylist = get_me_random_list(list_size)
            mylist.sort()
            start = time.time()
            # search function to test 
            binary_search_iterative(mylist, -1)
            end = time.time()
            sort_time = end - start
            total_time += sort_time
        
        avg_time = total_time / 100
        print(f"Avg time to sort a list of {list_size} using iterative binary search: {avg_time:0.08f} seconds")

    for list_size in list_sizes:
        total_time = 0
        for i in range(100):

            mylist = get_me_random_list(list_size)
            mylist.sort()
            start = time.time()
            # search function to test 
            binary_search_recursive(mylist, -1)
            end = time.time()
            sort_time = end - start
            total_time += sort_time
        
        avg_time = total_time / 100
        print(f"Avg time to sort a list of {list_size} using recursive binary search: {avg_time:0.08f} seconds")



