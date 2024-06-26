capital_premise = 600
capital_hypothesis = 300

# the hypothesis refers to James' capital, which is also mentioned in the premise
if capital_hypothesis >= capital_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif capital_hypothesis < capital_premise:
    # if the hypothesis value is less than the premise value, it entails the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
