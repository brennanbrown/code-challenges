// Given a random non-negative number, function returns 
// the digits of this number within an array in reverse order.
function digitize(n) {
    const Arr = Array.from(String(n), Number);
    return Arr.reverse();
  }
  
  Test.assertDeepEquals(digitize(35231),[1,3,2,5,3]);