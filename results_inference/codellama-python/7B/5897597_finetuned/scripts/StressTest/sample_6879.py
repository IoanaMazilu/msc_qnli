bonds_purchased_premise = 1500
bonds_purchased_hypothesis = 6500

# the hypothesis refers to the amount of US saving bonds purchased by Robert mentioned in the premise
if bonds_purchased_premise >= bonds_purchased_hypothesis:
    # check if the amount of 'bonds_purchased_premise' contradicts the estimate of less than 'bonds_purchased_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
