def merge_dicts(dict1, dict2):
    merged = dict1.copy() 
    merged.update(dict2) 
    return merged

# Проверка
if __name__ == "__main__":
    print(merge_dicts({'a': 2, 'b': 12}, {'c': 11, 'e': 5})) #{'a': 2, 'b': 12, 'c': 11, 'e': 5}
    print(merge_dicts({'a': 14, 'b': 12}, {'c': 11, 'a': 15})) #{'a': 15, 'b': 12, 'c': 11}
