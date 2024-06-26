units_digits_premise = 9
units_digits_hypothesis = 9

# the hypothesis refers to the units digits of Sophie Germain primes mentioned in the premise
if units_digits_hypothesis >= units_digits_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the units digits
    # any units digits less than 'units_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)