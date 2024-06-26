speed_premise = 40
speed_hypothesis = 70

# the hypothesis introduces a new limit on the speed, which is not present in the premise
if speed_premise >= speed_hypothesis:
    label = "contradiction"
elif speed_premise < speed_hypothesis:
    label = "neutral"
else:
    label = "entailment"

print(label)
