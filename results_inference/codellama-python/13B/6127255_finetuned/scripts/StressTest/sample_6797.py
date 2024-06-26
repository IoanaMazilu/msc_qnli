deposit_premise = 62500
deposit_hypothesis = 62500

# the hypothesis refers to the amount of money Lucy deposited, which is also mentioned in the premise
if deposit_hypothesis >= deposit_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
