# implement bubble sort

def bubble_sort(lst):
    for i in enumerate(lst):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                print(lst)
    return lst


print(bubble_sort([5, 3, 8, 6, 7, 2]))