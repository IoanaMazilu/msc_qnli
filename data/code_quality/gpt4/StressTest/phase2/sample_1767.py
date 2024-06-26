rent_cost_premise = 133
rent_cost_hypothesis = 533

# the hypothesis refers to the cost of tool rent mentioned in the premise
if rent_cost_premise >= rent_cost_hypothesis:
    # check if the estimate of 'rent_cost_premise' contradicts the less than 'rent_cost_hypothesis'
    label = "contradiction"
else:
    # if the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
