deposit_premise = 62500
deposit_hypothesis = 52500

# the hypothesis refers to the amount deposited by Lucy, which is also mentioned in the premise
if deposit_hypothesis!= deposit_premise:
    # check if the amount deposited in the hypothesis contradicts the amount deposited in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
