speed_premise = 40
speed_hypothesis = 70

# the hypothesis refers to the speed at which Bob drives
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # check if the hypothesis value is less than the premise value, but not contradicting it
    label = "neutral"
else:
    # if the hypothesis value is greater than or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
