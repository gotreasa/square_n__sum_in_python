def square_sum(values: list[int]):
    if not isinstance(values, list):
        raise ValueError("❗️ Input should be an array")
    if not all(isinstance(value, int) for value in values):
        raise ValueError("❗️ Input should be an array of numbers")
    result = 0
    for value in values:
        result += value**2
    return result
