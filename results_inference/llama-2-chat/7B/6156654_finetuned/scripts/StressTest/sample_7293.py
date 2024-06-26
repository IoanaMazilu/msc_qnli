capital_premise = 300
capital_hypothesis = 600

# the hypothesis refers to the capital of James mentioned in the premise
if capital_premise >= capital_hypothesis:
    # check if the premise value contradicts the hypothesis value
    label = "contradiction"
elif capital_premise < capital_hypothesis:
    # if the premise value is less than the hypothesis value, we can infer entailment
    label = "entailment"
else:
    # if the premise and hypothesis values are the same, we can infer neutral
    label = "neutral"

print(label)
