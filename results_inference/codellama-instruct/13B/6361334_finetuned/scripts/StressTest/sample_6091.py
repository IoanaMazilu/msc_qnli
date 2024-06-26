premise_prime = 3
hypothesis_prime = 2

# the hypothesis refers to the number of p + 1 that is prime, which is also mentioned in the premise
if hypothesis_prime <= premise_prime:
    # check if the hypothesis value contradicts the estimate of less than 'premise_prime'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of p + 1 that is prime
    # any number of p + 1 that is prime is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
