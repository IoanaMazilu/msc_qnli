units_digits_premise = 9
units_digits_hypothesis = 9

# the hypothesis refers to the possible units digits of Sophie Germain primes greater than less than 'units_digits_hypothesis'
if units_digits_hypothesis <= units_digits_premise:
    # check if the hypothesis value contradicts the estimate of more than 'units_digits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of units digits
    # any number of units digits greater than 'units_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
