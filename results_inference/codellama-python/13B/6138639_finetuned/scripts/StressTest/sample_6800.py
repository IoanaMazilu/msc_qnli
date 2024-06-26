bonds_purchased_premise = 4000
bonds_purchased_hypothesis = 5000

# the hypothesis refers to the amount of bonds purchased by Robert, which is also mentioned in the premise
if bonds_purchased_hypothesis!= bonds_purchased_premise:
    # check if the amount of bonds purchased in the hypothesis contradicts the amount of bonds purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
