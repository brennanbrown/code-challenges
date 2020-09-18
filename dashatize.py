import re

def dashatize(num):
    num = str(num)
    odds = [1, 3, 5, 7, 9]
    for i in odds:
        i = str(i)
        num = num.replace(i, "-" + i + "-")
    num = re.sub("-{2,}", "-", num)
    num = re.sub("^-|-$", "", num)
    return num

test.describe('Basic')
test.assert_equals(dashatize(274),"2-7-4", "Should return 2-7-4")
test.assert_equals(dashatize(5311),"5-3-1-1", "Should return 5-3-1-1")
test.assert_equals(dashatize(86320),"86-3-20", "Should return 86-3-20")
test.assert_equals(dashatize(974302),"9-7-4-3-02", "Should return 9-7-4-3-02")
test.describe('Weird')
test.assert_equals(dashatize(None),"None", "Should return None")
test.assert_equals(dashatize(0),"0", "Should return 0")
test.assert_equals(dashatize(-1),"1", "Should return 1")
test.assert_equals(dashatize(-28369),"28-3-6-9", "Should return 28-3-6-9")