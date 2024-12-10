def max_odd(array):
    odd_numbers = [x for x in array if isinstance(x, (int, float)) and x % 2 != 0]
    return max(odd_numbers, default=None)

print(max_odd([1, 2, 3, 4, 4])) # 3
print(max_odd([21.0, 2, 3, 4, 4])) # 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # 3
print(max_odd(['ololo', 'fufufu'])) # None
print(max_odd([2, 2, 4])) # None

