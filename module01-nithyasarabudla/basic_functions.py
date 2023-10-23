# 1: multiply that takes in two numbers and returns their product. For example, multiply(5, 10) should return 50.

def multiply(a, b):
    """ multiply that takes in two numbers and returns their product """
    return a * b


multiply(5, 10)


# 2: hello_name that takes in someone's name (a string) and returns "Hello, [Name]!".
# If no string is passed, return "Hello, you!".
# For example, hello_name("Akbar") should return Hello, Akbar! and hello_name() should return Hello, you!.

def hello_name(name="you"):
    """hello_name that takes in someone's name (a string) and returns "Hello, [Name]!".
 If no string is passed, return "Hello, you!"."""
    return "Hello, " + name + "!"


hello_name("Akbar")
hello_name()


# 3: less_than_ten that takes in a list of numbers and returns only the numbers that are less than 10.
# For example, less_than_ten([1, 5, 81, 10, 8, 2, 102]) should return [1, 5, 8, 2].

def less_than_ten(numbers):
    """less_than_ten that takes in a list of numbers and returns only the numbers that are less than 10."""
    result = []
    for x in numbers:
        if x < 10:
            result.append(x)
    return result


less_than_ten([1, 5, 81, 10, 8, 2, 102])
