import re

def name_list(list):
    list = list.upper()
    
    # Convert string into an array.
    array_list = list.split(";")
    # Switch first and last names.
    array_list = [":".join(n.split(":")[::-1]) for n in array_list]
    # List out names alphabetically.
    array_list = sorted(array_list)
    
    # Convert array back into string
    string = ")("
    list = string.join(array_list)
    
    # Use regex for proper output syntax
    list = re.sub(":", ", ", list)
    list = re.sub("^", "(", list)
    list = re.sub("$", ")", list)

    return list

def testing(s, exp):
    print("Testing:\n" + s)
    ans = name_list(s)
    print("ACTUAL =\n%s" % (ans))
    print("EXPECT =\n%s" % (exp))
    print(ans == exp)
    Test.assert_equals(ans, exp)

Test.describe("name_list")
Test.it("Basic tests")
def tests():
    testing("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn", 
            "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)")
    
    testing("John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Steve;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell", 
        "(BELL, MEGAN)(CORNWELL, AMBER)(DORNY, JAMES)(DORRIES, PAUL)(GATES, JOHN)(KERN, ANN)(KORN, ANNA)(META, ALEX)(RUSSEL, ELIZABETH)(STEVE, LEWIS)(WAHL, MICHAEL)")
    
    testing("Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:Dorries;Ann:Kern;Haley:Arno;Paul:Dorny;Madison:Kern", 
        "(ARNO, ALEX)(ARNO, HALEY)(BELL, SARAH)(CORNWELL, ALISSA)(DORNY, PAUL)(DORRIES, ANDREW)(KERN, ANN)(KERN, MADISON)")

tests()
print("<COMPLETEDIN::>")
print("<COMPLETEDIN::>")