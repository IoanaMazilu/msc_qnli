wheat_purchased_premise = 30
wheat_purchased_hypothesis = 60

# the hypothesis refers to the quantity of wheat purchased, also mentioned in the premise
if wheat_purchased_hypothesis < wheat_purchased_premise:
    # check if the quantity of 'wheat_purchased_hypothesis' contradicts the quantity of wheat purchased in the premise
    label = "contradiction"
elif wheat_purchased_hypothesis > wheat_purchased_premise:
    # check if the quantity of 'wheat_purchased_hypothesis' contradicts the quantity of wheat purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
