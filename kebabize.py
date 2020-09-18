# Using Regex
import re

def kebabize(string):
    # Convert all capital letters to lowercase
    # with a dash beforehand.
    string = re.sub(r'(?<!^)(?=[A-Z])', '-', string).lower()
    # Remove all numbers.
    string = ''.join([i for i in string if not i.isdigit()])
    # Remove dash at front of strings.
    string = re.sub('^-', '', string)
    return string

Test.describe("Basic tests")
Test.assert_equals(kebabize('myCamelCasedString'), 'my-camel-cased-string')
Test.assert_equals(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
Test.assert_equals(kebabize('SOS'), 's-o-s')
Test.assert_equals(kebabize('42'), '')
Test.assert_equals(kebabize('CodeWars'), 'code-wars')