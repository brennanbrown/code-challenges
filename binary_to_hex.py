def binary_to_hex(binary: str) -> str:
    return hex(int(binary, 2))[2:]

# This code converts the binary string to an integer using the int() function, and then converts the integer to a hexadecimal string using the hex() function. The [2:] at the end is used to strip off the "0x" prefix that hex() adds to the beginning of the string.

# Here is an example of how to use the function:

# binary string to convert
binary = "1101"

# convert binary to hexadecimal
hexadecimal = binary_to_hex(binary)

# print the result
print(hexadecimal)  # Output: "d"

# Alternatively, you can combine the two lines of code into a single line using a lambda function:

binary_to_hex = lambda binary: hex(int(binary, 2))[2:]

# This code creates a lambda function that takes a binary string as input and returns the corresponding hexadecimal string. The function works in the same way as the first example, but it is defined in a single line of code.

# Here is an example of how to use the lambda function:

# binary string to convert
binary = "1101"

# convert binary to hexadecimal
hexadecimal = binary_to_hex(binary)

# print the result
print(hexadecimal)  # Output: "d"
