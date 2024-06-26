bonds_purchased_premise = 1500
bonds_purchased_hypothesis = 7500

# the hypothesis refers to the amount of US saving bonds purchased by Robert, which is also mentioned in the premise
if bonds_purchased_hypothesis == bonds_purchased_premise:
    # check if the amount of bonds purchased in the hypothesis matches the amount mentioned in the premise
    label = "entailment"
elif bonds_purchased_hypothesis!= bonds_purchased_premise:
    # check if the amount of bonds purchased in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, but also cannot be explicitly entailed from the premise, we infer neutral
    label = "neutral"

print(label)
