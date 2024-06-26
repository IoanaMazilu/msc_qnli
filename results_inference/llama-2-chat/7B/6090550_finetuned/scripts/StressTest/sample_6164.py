# the hypothesis refers to the quantity of wheat purchased by Arun mentioned in the premise
if wheat_purchased_hypothesis!= wheat_purchased_premise:
    # check if the quantity of wheat purchased in the hypothesis contradicts the quantity in the premise
    label = "contradiction"
else:
    # if the quantity of wheat purchased in the hypothesis does not contradict the quantity in the premise, we can infer entailment
    label = "entailment"

print(label)
