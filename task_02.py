def coincidence(lst=None, rng=None):
    if lst is None or rng is None:
        return []
    return [item for item in lst if isinstance(item, (int, float)) and item in rng]

print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # [3, 4, 5]
print(coincidence()) # []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # [1, 2, 2.5]

