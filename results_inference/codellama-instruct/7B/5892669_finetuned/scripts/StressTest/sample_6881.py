bonds_purchased_premise = 1500
bonds_purchased_hypothesis = 7500

# the hypothesis refers to the amount of US saving bonds Robert purchased, mentioned in the premise
if bonds_purchased_hypothesis!= bonds_purchased_premise:
    # check if the amount of bonds purchased in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
