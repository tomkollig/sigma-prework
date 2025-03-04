from datetime import datetime


def calculate_age(date):
    today = datetime.now()
    date = datetime.strptime(date, "%d-%m-%Y")
    return today.year - date.year - ((today.month, today.day) < (date.month, date.day))


def run_tests():
    test_cases = [
        "01-01-1990",  # Expected: 35
        "04-12-1972"  # Expected: 52
    ]

    for test in test_cases:
        result = calculate_age(test)
        print(f"Input: {test}")
        print(f"Output: {result}")
        print("---")


run_tests()
