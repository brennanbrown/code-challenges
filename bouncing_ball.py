# Problem: A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known. 
# He drops the ball out of the window. The ball bounces a fraction of its height.
# His mother looks out of a window that's a certain amount of meters from the ground.
# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?)
def bouncing_ball(h, bounce, window):
    results = -1
    if (0 < bounce < 1):
        if h < window:
            results = 1
        new_h = h * bounce
        results = bouncing_ball(new_h, bounce, window) + 2
        return results
    return results

@test.describe('Tests')
def fixed_tests():
    def testing(h, bounce, window, exp):
        actual = bouncing_ball(h, bounce, window)
        Test.assert_equals(actual, exp)
        
    @test.it('Fixed Tests')
    def tests():
        testing(2, 0.5, 1, 1)
        testing(3, 0.66, 1.5, 3)
        testing(30, 0.66, 1.5, 15)
        testing(30, 0.75, 1.5, 21)