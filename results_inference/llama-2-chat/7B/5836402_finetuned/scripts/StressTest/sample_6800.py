purchase_value_premise = 4000
purchase_value_hypothesis = 5000

# the hypothesis refers to the value of the bonds purchased by Robert, mentioned in the premise
if purchase_value_premise!= purchase_value_hypothesis:
    # check if the value of the bonds in the hypothesis contradicts the value of the bonds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
