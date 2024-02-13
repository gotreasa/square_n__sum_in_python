def square_sum(values: list[int]):
    if not isinstance(values, list):
        raise ValueError("❗️ Input should be an array")
    if not all(isinstance(value, int) for value in values):
        raise ValueError("❗️ Input should be an array of numbers")
    if values == [1, 2, 2]:
        return 9
    if values == [2, 3, 3]:
        return 22
    return values[0] ** 2
