units_digits_premise = 1
units_digits_hypothesis = 4

# the hypothesis refers to the units digits of Sophie Germain primes, as mentioned in the premise
if units_digits_hypothesis <= units_digits_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise provides only an estimate for the units digits of Sophie Germain primes
    # any number greater than 'units_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
