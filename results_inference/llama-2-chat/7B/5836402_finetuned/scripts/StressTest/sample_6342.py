premise_sum = 288
hypothesis_sum = 588

# the hypothesis refers to the sum mentioned in the premise
if hypothesis_sum >= premise_sum:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
