capital_premise = 1250
capital_hypothesis = 7250

# the hypothesis refers to Ben's capital, mentioned also in the premise
if capital_hypothesis != capital_premise:
    # check if the hypothesis value contradicts the value of Ben's capital in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
