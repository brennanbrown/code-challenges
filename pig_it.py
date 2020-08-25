# Function moes the first letter of each word to the end of it, 
# then add "ay" to the end of the word. 
# Leave punctuation marks untouched.
def pig_it(words):
    pig_latin = []
    space = " "
    words = words.split()
    for word in words:
        if (word == "!") or (word == "?"):
            pig_latin.append(word[1:] + word[0])
        else:
            pig_latin.append(word[1:] + word[0] + "ay")

    return space.join(pig_latin)

Test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
Test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')