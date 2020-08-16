# Function takes in RGB decimal values will result in 
# a hexadecimal representation being returned. 
#
# Valid decimal values for RGB are 0 - 255. 
# Any values that fall out of that range must be rounded 
# to the closest valid value.
def rgb_to_hex(r, g, b):
    def clamp(x): 
        return max(0, min(x, 255))
    return ("{0:02X}" *3).format(clamp(r), clamp(g), clamp(b))

test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")