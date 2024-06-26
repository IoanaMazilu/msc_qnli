units_digits_premise = 7
units_digits_hypothesis = 8

# the hypothesis refers to the units digits of Sophie Germain primes, mentioned also in the premise
if units_digits_hypothesis <= units_digits_premise:
    # check if the hypothesis value contradicts the estimate of more than 'units_digits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the units digits
    # any number of units digits greater than 'units_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
