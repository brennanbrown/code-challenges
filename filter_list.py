# Function that takes a list of non-negative integers 
# and strings and returns a new list with the strings filtered out.
def filter_list(list):
    new_list = []
    for element in list:
        if type(element) is int:
            new_list.append(element)
    
    return new_list

test.assert_equals(filter_list([1,2,'a','b']),[1,2])
test.assert_equals(filter_list([1,'a','b',0,15]),[1,0,15])
test.assert_equals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])
