premise_prime = 10
hypothesis_prime = 10

# the hypothesis refers to the number of p and 2p+1 mentioned in the premise
if premise_prime <= hypothesis_prime:
    # check if the estimate of 'hypothesis_prime' contradicts the number of p in the premise
    label = "contradiction"
elif hypothesis_prime!= premise_prime:
    # check if the number of p in the hypothesis contradicts the number of p reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
