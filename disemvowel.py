# Function that takes a string and return a new string with all vowels removed.
def disemvowel(string):
    new_string = string
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
    for x in string:
        if x in vowels:
            new_string = new_string.replace(x,"");
    return new_string

test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
test.assert_equals(disemvowel("I can haz cheezburger?"), " cn hz chzbrgr?")
test.assert_equals(disemvowel("OMG this is simply le epic!!"), "MG ths s smply l pc!!")