amount_premise = 3600
amount_hypothesis = 3600

# the hypothesis refers to the amount from Anwar mentioned in the premise
if amount_hypothesis >= amount_premise:
    # check if the hypothesis value contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
