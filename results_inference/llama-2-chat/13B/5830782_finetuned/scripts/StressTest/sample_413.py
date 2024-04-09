# defining the ratio of ages in the premise and hypothesis
ratio_premise = 1/2
ratio_hypothesis = 1/2

# the hypothesis refers to the ratio of ages mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis value contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
