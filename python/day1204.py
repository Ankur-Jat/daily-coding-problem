import enum


def gcd(x, y):
    while y:
        x, y = y, y % x
    return x


def gcd_of_array(num_array):
    if not num_array:
        return None
    result = num_array[0]
    for num in num_array[1:]:
        result = gcd(result, num)
        if result == 1:
            return 1
    return result


def test():
    testcases = [
        [[1, 2, 3, 4, ], 1],
        [[56, 42, 14, ], 14],
        [[], None]
    ]
    for index, testcase in enumerate(testcases):
        assert gcd_of_array(
            testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
