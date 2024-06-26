pets_premise = 96
pets_hypothesis = 56

# the hypothesis refers to the total number of pets Claire has, which is also mentioned in the premise
if pets_hypothesis >= pets_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
