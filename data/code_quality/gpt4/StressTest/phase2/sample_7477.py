units_digit_premise = 7
units_digit_hypothesis = 8

# the hypothesis refers to the units digit of Sophie Germain primes mentioned in the premise
if units_digit_hypothesis < units_digit_premise:
    # check if the 'units_digit_hypothesis' contradicts the lower limit of the units digit in the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the units digit
    # any units digit greater than 'units_digit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
