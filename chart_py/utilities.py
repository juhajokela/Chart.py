
def combine(first, second):
    return [a + b for a, b in zip(first, second)]


def cumulate(array):
    result = []
    accumulator = 0
    for number in array:
        result.append(number + accumulator)
        accumulator += number
    return result
