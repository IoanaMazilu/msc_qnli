amount_premise = 450
amount_hypothesis = 750

# the hypothesis refers to the amount sold, also mentioned in the premise
if amount_hypothesis!= amount_premise:
    # check if the amount in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
