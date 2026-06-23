# BAD AND SIMPLE PROMPT USED: 
# "write a function that will square number in a list
# ? What a language? Any negative number? Any non-numbers? Return a new list?

def square_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
    return numbers

# Usage
nums = [1, 2, 3, 4, 5]
result = square_numbers(nums)
print(result)  # Output: [1, 4, 9, 16, 25]