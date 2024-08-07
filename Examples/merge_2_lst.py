# Create a function to merge two sorted lists into one sorted list.
def merge_sorted_lists(list1:list[int], list2:list[int]) -> list[int]:
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
            print(merged_list)
        else:
            merged_list.append(list2[j])
            j += 1
            print(merged_list) 

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

print(merge_sorted_lists([1, 3, 5, 7, 8], [2, 4, 6, 8, 8]))
