sold_value_premise = 450
sold_value_hypothesis = 750

# the hypothesis refers to the value of what was sold, which is also mentioned in the premise
if sold_value_premise!= sold_value_hypothesis:
    # check if the value in the hypothesis contradicts the value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
