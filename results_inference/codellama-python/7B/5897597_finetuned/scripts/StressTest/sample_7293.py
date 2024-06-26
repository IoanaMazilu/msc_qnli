capital_premise = 300
capital_hypothesis = 600

# the hypothesis refers to the amount of James' capital mentioned in the premise
if capital_premise >= capital_hypothesis:
    # check if the estimate of 'capital_hypothesis' contradicts the amount of capital in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)