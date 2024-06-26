deposit_premise = 62500
deposit_hypothesis = 52500
annual_return = 20

# the hypothesis refers to the amount of money deposited by Lucy, which is also mentioned in the premise
if deposit_hypothesis!= deposit_premise:
    # check if the amount of money deposited in the hypothesis contradicts the amount of money deposited in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
