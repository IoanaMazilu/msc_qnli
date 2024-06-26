wheat_purchased_premise = 30
wheat_purchased_hypothesis = 40

# the hypothesis refers to the quantity of wheat purchased mentioned in the premise
if wheat_purchased_premise >= wheat_purchased_hypothesis:
    # check if the estimate of 'wheat_purchased_hypothesis' contradicts the quantity of wheat purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
