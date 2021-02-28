
import random 
import time

def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list 


def insertion_sort(a_list):

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value


def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
            # print("After increments of size", sublist_count, "The list is", a_list)
    sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
    while position >= gap and a_list[position - gap] > current_value:
        a_list[position] = a_list[position - gap]
        position = position - gap
    
    a_list[position] = current_value

def python_sort(a_list):
    return sorted(a_list)


if __name__ == "__main__":

    random.seed(100)

    list_sizes = [500, 1000, 3000]

    total_time = 0

    for list_size in list_sizes:
        for i in range(100):

            mylist = get_me_random_list(list_size)
            start = time.time()
            # sort function to test 
            insertion_sort(mylist)
            end = time.time()
            sort_time = end - start
            total_time += sort_time
        
        avg_time = total_time / 100
        print(f"Avg time to sort a list of {list_size} using insertion sort: {avg_time:0.08f} seconds")
    
    for list_size in list_sizes:
        for i in range(100):
            mylist = get_me_random_list(list_size)
            start = time.time()
            # sort function to test 
            ordered_list = python_sort(mylist)
            end = time.time()
            sort_time = end - start
            total_time += sort_time
        
        avg_time = total_time / 100
        print(f"Avg time to sort a list of {list_size} using python_sort: {avg_time:0.08f} seconds")