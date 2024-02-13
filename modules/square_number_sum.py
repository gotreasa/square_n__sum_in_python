def square_sum(numbers: list[int]):
    if not isinstance(numbers, list):
        raise ValueError("❗️ Input should be an array")
    if not all(isinstance(number, int) for number in numbers):
        raise ValueError("❗️ Input should be an array of numbers")
    result = 0
    for number in numbers:
        result += number**2
    return result
