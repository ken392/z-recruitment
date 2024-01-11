/**
*  Please take a look problem65.png in advance
* 
* the sequence of partial values of continued fractions for e
* {2/1, 3/1, 8/3, 11/4, 19/7, 87/32....}
* 
* legend: 
* numerators: subset of numerators of above sequence
* continued_fractions: subset of continued fraction values
* 
* the continued fraction has the pattern with 1, 2k, 1
* k | numerators | continued_fractions
* 1 | 2         | 1
* 2 | 3         | 2
* 3 | 8         | 1
* 4 | 11        | 1
* 5 | 19        | 4
* 6 | 87        | 1
 */

// when k = 1 the numerator is 2 (numerators[0])
const initialNumerator = 2;

const sumOfNumerator = (nth) => {
  // numerators[n]
  let currentNumerator = initialNumerator;
  // continued_fractions[n-1]
  let previousNumerator = 1;

  // continued_fractions[n-1]
  let continuedFraction = 1;
  let prePreNumerator;

  // Calculate current numerator
  // O(n)  time complexity
  for (let k = 2; k <= nth; k++) {
    // numerators[n-2]
    prePreNumerator = previousNumerator;

    if (k % 3 === 0) {
      // if k = 3n, previous continued fraction is 2(k/3)
      continuedFraction = 2 * Number(k / 3);
    } else {
      // otherwise 1
      continuedFraction = 1;
    }
    // update previous numerator
    previousNumerator = currentNumerator;

    // update current numerator
    // numerator[n] = numerator[n-1] * contienued faction[n-1] + 1 * numerator[n-2]
    currentNumerator = continuedFraction * previousNumerator + prePreNumerator;

  }

  const sum = sumOfDigits(currentNumerator)
  console.log(currentNumerator, sum);
}

const sumOfDigits = (integer) => {
  // Convert the integer to a string to easily access individual digits
  const digits = String(integer).split('');

  // Use Array.reduce() to calculate the sum of digits
  const sum = digits.reduce((acc, digit) => acc + parseInt(digit, 10), 0);

  return sum;
}

sumOfNumerator(10)
