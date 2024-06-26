rental_cost_premise = 160
rental_cost_hypothesis = 360

# the hypothesis refers to the rental cost mentioned in the premise
if rental_cost_hypothesis <= rental_cost_premise:
    # check if the estimate of'rental_cost_hypothesis' contradicts the rental cost in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
