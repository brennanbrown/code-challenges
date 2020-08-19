// Function returns the number (count) of vowels in the given string. 
function getCount(str) {
    var vowelsCount = str.match(/[aeiou]/gi);
    if (vowelsCount != null) {
      return vowelsCount.length;
    } else return 0;
  }
  
  describe("Case 1", function(){
    it ("should be defined", function(){
        Test.assertEquals(getCount("abracadabra"), 5)
    });
  });
  
  // Function is given a string of space separated numbers, 
  // and has to return the highest and lowest number.
  function highAndLow(numbers){
    let arr = numbers.split(' ').map(function(i) {
      return parseInt(i, 10);
    });
    let max = Math.max(...arr);
    let min = Math.min(...arr);
    return max.toString() + " " + min.toString();
  }
  
  Test.assertEquals(highAndLow("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");