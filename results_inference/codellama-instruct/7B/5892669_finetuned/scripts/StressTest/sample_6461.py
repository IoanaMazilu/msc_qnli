deposit_premise = 62500
deposit_hypothesis = 52500

# the hypothesis refers to the amount of money deposited by Lucy, mentioned in the premise
if deposit_hypothesis!= deposit_premise:
    # check if the amount of money deposited in the hypothesis contradicts the amount of money deposited in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
