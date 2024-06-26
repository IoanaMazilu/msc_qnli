speed_premise = 30
speed_hypothesis = 50

# the hypothesis refers to the speed of driving from City A to City B, mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the premise value
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise value, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
