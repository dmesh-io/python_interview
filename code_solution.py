"""
The very first mistake is indentation in the "if __name__ == '__main__':" part.

The first mistake is that the function returns the value of total instead of average.
This means that it returns the sum of all the numbers in the list instead of their average.

The second mistake is that the function does not handle the case where the input list is empty.
If an empty list is passed to this function, it will raise a ZeroDivisionError because it tries to divide by zero
when calculating the average.

The fourth "mistake" is that there’s no need to initialize variable total with value 0
since we can use built-in function sum() to get sum of all elements in list.


"""


# A corrected version of this function might look like this:
def calculate_average(numbers):
    if not numbers:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    return average


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    result = calculate_average(numbers)
    assert result == 2.5

    numbers2 = []
    result2 = calculate_average(numbers2)

    print(f"The average is: {result}")
