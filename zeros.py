# Function calculates the number of trailing zeros in a factorial of a given number.
def zeros(n):
    x = n // 5
    y = x 
    while x > 0:
        x /= 5
        y += int(x)
    return y

test.describe("Sample Tests")
test.it("Should pass sample tests")
test.assert_equals(zeros(0), 0, "Testing with n = 0")
test.assert_equals(zeros(6), 1, "Testing with n = 6")
test.assert_equals(zeros(30), 7, "Testing with n = 30")