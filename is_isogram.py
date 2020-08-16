# Function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.
def is_isogram(string):
    string = string.lower()
    for i in range(len(string)): 
        for j in range(i + 1, len(string)):  
            if(string[i] == string[j]): 
                return False
    return True

Test.assert_equals(is_isogram("Dermatoglyphics"), True )
Test.assert_equals(is_isogram("isogram"), True )
Test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
Test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
Test.assert_equals(is_isogram("isIsogram"), False )
Test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )