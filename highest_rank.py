# Function returns the number which is most 
# frequent in the given input array. 
# If there is a tie for most frequent number, 
# return the largest number among them.
def highest_rank(List):
    List = sorted(List, reverse = True)
    counter = 0
    num = List[0] 

    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency > counter): 
            counter = curr_frequency 
            num = i 
    
    return num 

test.describe("Example Tests")
test.it("Example Test Case")
test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)