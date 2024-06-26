bonds_purchased_premise = 1500
bonds_purchased_hypothesis = 6500

# the hypothesis refers to the amount of US saving bonds Robert purchased, mentioned in the premise
if bonds_purchased_premise >= bonds_purchased_hypothesis:
    # check if the estimate of 'bonds_purchased_hypothesis' contradicts the amount of bonds purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
