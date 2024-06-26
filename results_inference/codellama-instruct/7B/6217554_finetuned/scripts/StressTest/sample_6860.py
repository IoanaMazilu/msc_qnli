rate_premise = 4
rate_hypothesis = 4

# the hypothesis refers to the walking rate mentioned in the premise
if rate_hypothesis <= rate_premise:
    # check if the hypothesis value contradicts the walking rate in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
