speed_premise = 40
speed_hypothesis = 30

# the hypothesis refers to the driving speed from City A to City B, mentioned in the premise
if speed_hypothesis == speed_premise:
    # check if the driving speed in the hypothesis matches the driving speed reported in the premise
    label = "entailment"
else:
    # if the driving speed in the hypothesis does not match the driving speed in the premise, we can infer contradiction
    label = "contradiction"

print(label)
