# Function taking a positive integer as its 
# parameter and returning a string containing 
# the Roman Numeral representation of that integer.
ROMAN = [(1000, "M" ),( 900, "CM"),( 500, "D"),
        (  400, "CD"),( 100, "C" ),(  90, "XC"),
        (   50, "L" ),(  40, "XL"),(  10, "X"),
        (    9, "IX"),(   5, "V" ),(   4, "IV"),
        (    1, "I"),]

def arabic_to_roman(number):
    result = []
    for (arabic, roman) in ROMAN:
        (factor, number) = divmod(number, arabic)
        result.append(roman * factor)
        if number == 0:
            break
    return "".join(result)

test.assert_equals(arabic_to_roman(1),'I', "solution(1),'I'")
test.assert_equals(arabic_to_roman(4),'IV', "solution(4),'IV'")
test.assert_equals(arabic_to_roman(6),'VI', "solution(6),'VI'")
test.assert_equals(arabic_to_roman(14),'XIV', "solution(14),'XIV")
test.assert_equals(arabic_to_roman(21),'XXI', "solution(21),'XXI'")
test.assert_equals(arabic_to_roman(89),'LXXXIX', "solution(89),'LXXXIX'")
test.assert_equals(arabic_to_roman(91),'XCI', "solution(91),'XCI'")
test.assert_equals(arabic_to_roman(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
test.assert_equals(arabic_to_roman(1000), 'M', 'solution(1000), M')
test.assert_equals(arabic_to_roman(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
test.assert_equals(arabic_to_roman(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")