# A Narcissistic Number is a positive number which is the sum 
# of its own digits, each raised to the power of the number of 
# digits in a given base. 
#
# Eg. 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
#
# Function returns true or false depending upon whether the 
# given number is a Narcissistic number in base 10.
import math

def narcissistic(value):
    digits = int(math.log10(value))+1
    list = [int(d) for d in str(value)]
    nar_list = []
    
    for i in list:
        nar_value = i ** digits
        nar_list.append(nar_value)
    
    nar_sum = sum(nar_list)
    
    if nar_sum == value:
        return True
    
    return False

test.assert_equals(narcissistic(7), True, '7 is narcissistic');
test.assert_equals(narcissistic(371), True, '371 is narcissistic');
test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
test.assert_equals(narcissistic(1634), True, '4887 is narcissistic')
test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')