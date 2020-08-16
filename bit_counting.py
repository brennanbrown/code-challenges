# Function that takes an integer as input, and returns the number of bits 
# that are equal to one in the binary representation of that number. 
# You can guarantee that input is non-negative.
def bit_counting(number):
    binary_number = "{0:b}".format(number)
    sum_of_digits = sum(int(digit) for digit in str(binary_number))
    return sum_of_digits

test.assert_equals(countBits(0), 0);
test.assert_equals(countBits(4), 1);
test.assert_equals(countBits(7), 3);
test.assert_equals(countBits(9), 2);
test.assert_equals(countBits(10), 2);