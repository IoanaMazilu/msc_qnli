directors_per_charity_premise = 8
directors_per_charity_hypothesis = 8

# the hypothesis refers to the number of directors per charity mentioned in the premise
if directors_per_charity_hypothesis >= directors_per_charity_premise:
    # check if the hypothesis value contradicts the exact number of directors per charity in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
