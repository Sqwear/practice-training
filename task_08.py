from math import prod

def multiply_numbers(inputs=None):
    if inputs is None:
        return None
    if isinstance(inputs, (int, float)):
        inputs = str(inputs)
    if isinstance(inputs, str):
        digits = [int(char) for char in inputs if char.isdigit()]
        return prod(digits) if digits else None
    if isinstance(inputs, list):
        return prod([x for x in inputs if isinstance(x, int)])
    return None

print(multiply_numbers()) # None
print(multiply_numbers('ss')) # None
print(multiply_numbers('1234')) # 24
print(multiply_numbers('sssdd34')) # 12
print(multiply_numbers(2.3)) # 6
print(multiply_numbers([5, 6, 4])) # 120
