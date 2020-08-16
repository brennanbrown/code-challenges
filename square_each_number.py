# Function to square every digit of a number.
# Eg. 9119 will become 811181, because 9^2 is 81 and 1^2 is 1.
def square_each_number(num):
    result= ''
    list = [int(d) for d in str(num)]
    square_list = [i ** 2 for i in list]
    for i in square_list:
        result += str(i)
    return float(result)

test.assert_equals(square_digits(9119), 811181)