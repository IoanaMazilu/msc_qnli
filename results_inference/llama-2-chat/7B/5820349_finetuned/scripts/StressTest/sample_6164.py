wheat_purchased_premise = 30
wheat_purchased_hypothesis = 30

# the hypothesis refers to the amount of wheat purchased mentioned in the premise
if wheat_purchased_hypothesis >= wheat_purchased_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
