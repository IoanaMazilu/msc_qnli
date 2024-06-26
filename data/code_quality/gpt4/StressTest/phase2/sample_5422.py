capital_premise = 720
capital_hypothesis = 120

# the hypothesis refers to the capital of Thomas mentioned in the premise
if capital_hypothesis >= capital_premise:
    # check if the hypothesis value contradicts the estimate of less than 'capital_premise'
    label = "contradiction"
elif capital_hypothesis < capital_premise:
    # the premise gives only an estimate for the capital
    # any capital less than 'capital_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
