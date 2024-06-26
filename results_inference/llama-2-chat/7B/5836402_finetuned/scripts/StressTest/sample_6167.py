amount_premise = 95
amount_hypothesis = 95

# the hypothesis talks about the amount given to John, which is also mentioned in the premise
if amount_hypothesis >= amount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif amount_hypothesis < amount_premise:
    # check if the hypothesis value is less than the premise value, which implies entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
