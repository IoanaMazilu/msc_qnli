deposit_premise = 62500
deposit_hypothesis = 52500

# the hypothesis refers to the deposit amount mentioned in the premise
if deposit_hypothesis!= deposit_premise:
    # check if the deposit amount in the hypothesis contradicts the deposit amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
