sophie_germain_primes_premise = 8
sophie_germain_primes_hypothesis = 7

# the hypothesis talks about the product of units digits of Sophie Germain primes, referenced also in the premise
if sophie_germain_primes_hypothesis <= sophie_germain_primes_premise:
    # check if the hypothesis value contradicts the estimate of the product of units digits of Sophie Germain primes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of units digits of Sophie Germain primes
    # any product of units digits greater than'sophie_germain_primes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
