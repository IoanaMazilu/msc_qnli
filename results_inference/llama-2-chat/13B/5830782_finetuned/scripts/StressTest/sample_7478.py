units_digits_sophie_germain_primes_premise = 8
units_digits_sophie_germain_primes_hypothesis = 4

# the hypothesis talks about the product of the possible units digits of Sophie Germain primes, referenced also in the premise
if units_digits_sophie_germain_primes_hypothesis >= units_digits_sophie_germain_primes_premise:
    # check if the hypothesis value contradicts the estimate of greater than 'units_digits_sophie_germain_primes_premise'
    label = "contradiction"
elif units_digits_sophie_germain_primes_hypothesis < units_digits_sophie_germain_primes_premise:
    # the premise gives an estimate for the units digits of Sophie Germain primes
    # any number of units digits less than 'units_digits_sophie_germain_primes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
