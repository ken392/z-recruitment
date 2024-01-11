# The sequence of partial values of continued fractions for e
# {2/1, 3/1, 8/3, 11/4, 19/7, 87/32....}
# 
# legend: 
# numerators: subset of numerators of above sequence
# continued_fractions: subset of continued fraction values
# 
# the continued fraction has the pattern with 1, 2k, 1
# k | numerators | continued_fractions
# 1 | 2         | 1
# 2 | 3         | 2
# 3 | 8         | 1
# 4 | 11        | 1
# 5 | 19        | 4
# 6 | 87        | 1

# when k = 1 the numerator is 2 (numerators[0])
INITIAL_NUMERATOR = 2

def sum_of_numerator(nth):
  # numerators[n]
  current_numerator = INITIAL_NUMERATOR
  # numerators[n-1]
  previous_numerator = 1
  # continued_fractions[n-1]
  previous_continued_fraction = 0 

  # calculate current numerator
  # O(n) time complexity
  # 
  # the formula to detect current numerator is
  # current_numerator = numerators[n-1] * continued_fractions[n-1] + numerators[n-2]
  # 
  for k in range(2, nth + 1):
    # numerators[n-2]
    prepre_numerator = previous_numerator

    if( k % 3 == 0):
      # if k = 3n, previous continued fraction is 2k
      previous_continued_fraction = 2 * int(k/3)
    else: 
      # otherwise 1
      previous_continued_fraction = 1

    # update previous numerator
    previous_numerator = current_numerator

    # update current numerator
    # numerator[n] = numerator[n-1] * contienued faction[n-1] + 1 * numerator[n-2]
    current_numerator = previous_numerator * previous_continued_fraction + prepre_numerator

    # dump values
    # print("{:3} | {:4} | {:2}".format(k,  current_numerator, previous_continued_fraction))

  result = sum_of_digits(current_numerator)
  print("sum of {}th numerator is {} (numerator:{})".format(nth, result, current_numerator))
  return result

def sum_of_digits(number):
    digits = [int(digit) for digit in str(number)]
    digit_sum = sum(digits)
    
    return digit_sum

sum_of_numerator(100)
