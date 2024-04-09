digits_premise = [8]
digits_hypothesis = [9]

# the hypothesis refers to the product of all possible units digits of Sophie Germain primes greater than 9
if all(digits_hypothesis[i] > digits_premise[i] for i in range(len(digits_premise))):
    # the hypothesis contradicts the premise, as the product of all possible units digits of Sophie Germain primes greater than 9 is not greater than the product of all possible units digits of Sophie Germain primes greater than 8
    label = "contradiction"
else:
    # the premise only gives an estimate for the product of all possible units digits of Sophie Germain primes greater than 8
    # any product of all possible units digits of Sophie Germain primes greater than 9 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
