# a better prompt: 
# "Write a Python function that takes a list of integers and returns a new list where each number is squared, excluding any negative numbers."
# ! This prompt shows:
# Language we want to use; The goal of the function; Constraints; Expected input type

'''
def square_numbers(numbers):
    """
    Takes a list of integers and returns a new list where each number 
    is squared, excluding any negative numbers.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of squared positive integers
    """
    return [x**2 for x in numbers if x >= 0]

# Usage examples
result = square_numbers([1, -2, 3, -4, 5])
print(result)  # Output: [1, 9, 25]

result = square_numbers([-10, -5, 0, 5, 10])
print(result)  # Output: [0, 25, 100]

result = square_numbers([-1, -2, -3])
print(result)  # Output: []
'''

# improved this prompt replying with context:
# "You don't take a list of integers; you pre-create many lists of integers. I didn't ask you this.
# When I ask 'write a Python function THAT TAKES a list of integers', the function needs to TAKE a list of integers, 
# which means the function needs an input of numbers from the user to TAKE a list of numbers to square them after.
# Understand now?"

def square_numbers():
    """
    Takes a list of integers from user input and returns a new list 
    where each number is squared, excluding any negative numbers.
    
    Returns:
        List of squared positive integers
    """
    # Get input from user
    user_input = input("Enter integers separated by spaces: ")
    
    # Convert string input to list of integers
    numbers = list(map(int, user_input.split()))
    
    # Square and filter out negative numbers
    squared = [x**2 for x in numbers if x >= 0]
    
    return squared

# Usage
if __name__ == "__main__":
    result = square_numbers()
    print("Squared positive numbers:", result)