# Remove duplicates from a list
mylist = ["apple", "banana", "cherry", "apple", "cherry"]

def remove_duplicates_dict(lst):

    # using dictionary
    return list(dict.fromkeys(lst))

def remove_duplicates_set(lst):

    # using set
    return list(set(lst)) 

newlist_dict = remove_duplicates_dict(mylist)
print(mylist) 
print(newlist_dict)
print("-------")

newlist_set = remove_duplicates_set(mylist)
print(newlist_set)


def remove_duplicates_no_conversion(lst):
 
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

newlist_no_conversion = remove_duplicates_no_conversion(mylist)
print(newlist_no_conversion)
