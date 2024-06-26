premise_prime = 2
hypothesis_prime = 3

# the hypothesis refers to the number of prime numbers less than 'hypothesis_prime'
if hypothesis_prime <= premise_prime:
    # check if the hypothesis value contradicts the estimate of 'premise_prime'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of prime numbers
    # any number of prime numbers greater than 'premise_prime' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
