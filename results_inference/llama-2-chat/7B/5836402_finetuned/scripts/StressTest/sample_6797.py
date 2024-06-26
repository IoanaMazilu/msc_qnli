deposit_premise = 62500
deposit_hypothesis = 62500

# the hypothesis refers to the deposit amount mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the hypothesis value contradicts the deposit amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the deposit amount in the premise, we can infer entailment
    label = "entailment"

print(label)
