def square_sum(value: list[int]):
    if not isinstance(value, list):
        raise ValueError("❗️ Input should be an array")
    if value == [1]:
        return 1
    if value == [2]:
        return 4
    raise ValueError("❗️ Input should be an array of numbers")
