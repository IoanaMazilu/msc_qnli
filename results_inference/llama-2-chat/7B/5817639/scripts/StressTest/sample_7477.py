possible_units_digits_premise = 7
possible_units_digits_hypothesis = 8

# the hypothesis talks about the product of units digits of Sophie Germain primes, referenced also in the premise
if possible_units_digits_hypothesis <= possible_units_digits_premise:
    # check if the hypothesis value contradicts the estimate of the product of units digits in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of units digits
    # any product of units digits greater than 'possible_units_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
