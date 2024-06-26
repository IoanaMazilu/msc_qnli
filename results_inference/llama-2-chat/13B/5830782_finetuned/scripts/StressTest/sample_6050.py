money_premise = 95
money_hypothesis = 55

# the hypothesis refers to the amount of money mentioned in the premise
if money_premise!= money_hypothesis:
    # check if the amount of money in the hypothesis contradicts the amount of money in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
