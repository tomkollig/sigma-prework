def maxmin(list):

    if not list:
        return None

    max = list[0]
    min = list[0]
    for number in list[1:]:
        if number > max:
            max = number
        elif number < min:
            min = number
    return [min, max]


def run_tests():
    test_cases = [
        [2, 4, 1, 0, 2, -1],  # Expected: [-1, 4]
        [20, 50, 12, 6, 14, 8],  # Expected: [6, 50]
        [100, -100],  # Expected: [-100, 100]
        [5],  # Expected: [5, 5]
        []  # Expected: None
    ]

    for test in test_cases:
        result = maxmin(test)
        print(f"Input: {test}")
        print(f"Output: {result}")
        print("---")


run_tests()
