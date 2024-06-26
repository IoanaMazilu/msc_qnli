prime_premise = 2
prime_hypothesis = 8

# the hypothesis talks about the same concept as the premise
if prime_hypothesis <= prime_premise:
    # check if the hypothesis value contradicts the estimate of 'prime_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'prime_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
