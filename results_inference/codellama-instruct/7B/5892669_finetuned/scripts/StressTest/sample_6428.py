sold_premise = 450
sold_hypothesis = 750

# the hypothesis refers to the amount of money that was sold, mentioned in the premise
if sold_hypothesis!= sold_premise:
    # check if the amount of money sold in the hypothesis contradicts the amount of money sold reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
