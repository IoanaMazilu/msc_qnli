units_digits_premise = 8
units_digits_hypothesis = 9

# the hypothesis refers to the number of units digits of Sophie Germain primes mentioned in the premise
if units_digits_hypothesis <= units_digits_premise:
    # check if the hypothesis value contradicts the estimate of more than 'units_digits_premise'
    label = "contradiction"
else:
    # any number of units digits greater than 'units_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)