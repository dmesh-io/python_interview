"""
The calculate_average function is supposed to calculate the average of a list of numbers.
However, it contains several mistakes that prevent it from working correctly.
Can you correct the mistakes?
Can you make it more efficient?

What if the input `numbers` is an empty list? It should return 0.
Can you update the print message using f-strings?
The output should be:
- 'The average is: 2.5'
"""


def calculate_average(numbers):
    total = 0
    for i in numbers:
        total += i
    average = total / len(numbers)
    return total


if __name__ == '__main__':
numbers = [1, 2, 3, 4]
result = calculate_average(numbers)
assert result == 2.5

numbers2 = []
calculate_average(numbers2)

print(result)
