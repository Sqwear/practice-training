def connect_dicts(dict1, dict2):
    if sum(dict1.values()) < sum(dict2.values()):
        dict1, dict2 = dict2, dict1
    result = {k: v for k, v in dict1.items() if v >= 10}
    result.update({k: v for k, v in dict2.items() if v >= 10 and k not in result})
    return dict(sorted(result.items(), key=lambda item: item[1]))

print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5})) # {"c": 11, "b": 12}
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15})) # {"d": 11, "c": 12, "a": 13}
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15})) # {"c": 11, "b": 12, "a": 15}
