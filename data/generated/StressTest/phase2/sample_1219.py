# Premise: The product of all the possible units digits of Sophie Germain primes greater than more than 1 is.
# Hypothesis: The product of all the possible units digits of Sophie Germain primes greater than 3 is.
# Golden Label: neutral

units_digits_sophie_primes_premise = 1
units_digits_sophie_primes_hypothesis = 3

# the hypothesis talks about the product of all possible units digits of Sophie Germain primes,
# which is also referenced in the premise
if units_digits_sophie_primes_hypothesis <= units_digits_sophie_primes_premise:
    # check if the hypothesis value contradicts the premise value of more than 'units_digits_sophie_primes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the units digits of Sophie Germain primes
    # any number greater than 'units_digits_sophie_primes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

