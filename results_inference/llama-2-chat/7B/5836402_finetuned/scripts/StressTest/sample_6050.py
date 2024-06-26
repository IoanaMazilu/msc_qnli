amount_premise = 95
amount_hypothesis = 55

# the hypothesis refers to the amount of money mentioned in the premise
if amount_premise!= amount_hypothesis:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
