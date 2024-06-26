wheat_purchased_premise = 30
wheat_purchased_hypothesis = 40

# the hypothesis refers to the amount of wheat purchased mentioned in the premise
if wheat_purchased_premise >= wheat_purchased_hypothesis:
    # check if the amount of 'wheat_purchased_premise' contradicts the estimate of less than 'wheat_purchased_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
