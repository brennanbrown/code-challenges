// Function squares each number passed into it and then sums the results together.
function squareSum(numbers){
    let arr = [];
    for (var i = 0, len = numbers.length; i < len; i++) {
      arr.push(numbers[i] * numbers[i]);
    }
    arr = arr.reduce((a, b) => a + b, 0);
    return arr;
  }
  
  Test.assertEquals(squareSum([1,2]), 5)
  Test.assertEquals(squareSum([0, 3, 4, 5]), 50)