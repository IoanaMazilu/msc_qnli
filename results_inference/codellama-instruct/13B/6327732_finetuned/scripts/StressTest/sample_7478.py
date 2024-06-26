premise_units_digits = 8
hypothesis_units_digits = 4

# the hypothesis refers to the number of Sophie Germain primes greater than 4, which is less than the number of primes greater than 8 mentioned in the premise
if hypothesis_units_digits >= premise_units_digits:
    # check if the hypothesis value contradicts the number of Sophie Germain primes greater than 8 mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Sophie Germain primes greater than 8
    # any number of Sophie Germain primes greater than 4 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
