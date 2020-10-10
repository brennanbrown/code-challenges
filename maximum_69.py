class Solution:
    def maximum_69(self, num):
        x = str(num)
        if "6" in x:
            x = x.replace("6", "9", 1)
        
        return int(x)