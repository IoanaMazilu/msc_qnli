deposit_premise = 62500
deposit_hypothesis = 52500

# the hypothesis refers to the amount of money deposited by Lucy, mentioned in the premise
if deposit_premise!= deposit_hypothesis:
    # check if the deposit amount in the hypothesis contradicts the deposit amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
