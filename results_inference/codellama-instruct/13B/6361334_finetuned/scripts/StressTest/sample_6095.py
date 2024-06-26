premise_units_digits = 9
hypothesis_units_digits = 8

# the hypothesis refers to the units digits of Sophie Germain primes greater than 'premise_units_digits'
if hypothesis_units_digits < premise_units_digits:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the units digits of Sophie Germain primes
    # any number of units digits greater than 'premise_units_digits' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
