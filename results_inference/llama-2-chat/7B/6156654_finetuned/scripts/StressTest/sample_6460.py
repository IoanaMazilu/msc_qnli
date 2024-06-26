deposit_premise = 72500
deposit_hypothesis = 62500

# the hypothesis refers to the deposit amount mentioned in the premise
if deposit_hypothesis!= deposit_premise:
    # check if the deposit amount in the hypothesis contradicts the deposit amount in the premise
    label = "contradiction"
else:
    # if the deposit amount in the hypothesis is equal to the deposit amount in the premise, we can infer entailment
    label = "entailment"

print(label)
