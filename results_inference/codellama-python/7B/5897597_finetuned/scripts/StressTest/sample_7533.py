weight_gain_premise = 10
weight_gain_hypothesis = 50

# the hypothesis refers to the weight gain of Leo mentioned in the premise
if weight_gain_hypothesis <= weight_gain_premise:
    # check if the hypothesis value contradicts the weight gain in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
