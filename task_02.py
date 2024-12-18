def filter_elements(lst, rng):
    start, stop = rng.start, rng.stop
    return [x for x in lst if isinstance(x, (int, float)) and start <= x < stop]

if __name__ == "__main__":
    print(filter_elements([1, 2, 3, 4, 5], range(3, 6))) #[3, 4, 5]
    print(filter_elements([], range(3, 6))) #[]
    print(filter_elements([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) #[1, 2, 2.5]
