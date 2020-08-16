# Function likes :: [String] -> String, which must take in input array, 
# containing the names of people who like an item. 
# It must return the display text as shown in the examples:
def facebook_likes(names):
    if (len(names) == 0):
        return("no one likes this")
    if (len(names) == 1):
        names = " ".join(names)
        return(names + " likes this")
    if (len(names) == 2):
        return(names[0] + " and " + names[1] + " like this")
    if (len(names) == 3):
        return(names[0] + ", " + names[1] + " and " + names[2] + " like this")
    if (len(names) > 3):
        remainder = (len(names) - 2)
        return(names[0] + ", " + names[1] + " and " + str(remainder) + " others like this")

Test.assert_equals(likes([]), 'no one likes this')
Test.assert_equals(likes(['Peter']), 'Peter likes this')
Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')