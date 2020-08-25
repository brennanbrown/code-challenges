# Function takes any string and truncates into a title-case, 
# single entity with a "#" in front, if under 140 characters. 
def generate_hashtag(s):
    if (len(s) > 0 and len(s) < 140):
        s = s.title()
        s = "#{0}".format(s)
        s = s.replace(" ", "")
        return s.strip()
    return False

Test.describe("Basic tests")
Test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
Test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expected a Hashtag (#) at the beginning.')
Test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
Test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
Test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
Test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
Test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
Test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
Test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')