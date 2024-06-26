premise = "The product of all the possible units digits of Sophie Germain primes greater than 9 is."
hypothesis = "The product of all the possible units digits of Sophie Germain primes greater than less than 9 is."

# the hypothesis refers to the number of Sophie Germain primes greater than 9 mentioned in the premise
if premise.count("greater than 9")!= hypothesis.count("greater than less than 9"):
    # check if the hypothesis value contradicts the number of Sophie Germain primes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Sophie Germain primes
    # any number of Sophie Germain primes greater than 9 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
