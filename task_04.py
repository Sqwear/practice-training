def sort_list(lst):
    if not lst:
        return []
    min_val, max_val = min(lst), max(lst)
    lst = [max_val if x == min_val else min_val if x == max_val else x for x in lst]
    lst.append(min_val)
    return lst

print(sort_list([])) # []
print(sort_list([2, 4, 6, 8])) # [8, 4, 6, 2, 2]
print(sort_list([1])) # [1, 1]
print(sort_list([1, 2, 1, 3])) # [3, 2, 3, 1, 1]

