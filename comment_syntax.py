# single-line comment with the hash character at the start of the line

print 1 + 2 * 3 # single-line comment at the end of the line

# multi-line comments with three double quotes to open the comment and another three double quotes to end it
def add(a, b):
    """Function brief description: Add two numbers or concatenate two strings

    Function detailed description: Function to add two numbers or
    to concatentate two strings

    Args:
        a: can be a number or a string
        b: can be a number or a string

    Returns:
        Addition of two numbers or concatenation of two strings

    """
    return a + b

print add(1, 2)

print add('note', 'book')
