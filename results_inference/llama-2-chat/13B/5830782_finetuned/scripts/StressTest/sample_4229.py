speed_premise = 30
speed_hypothesis = 30

# the hypothesis refers to the driving speed from City A to City B mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis speed contradicts the premise speed
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise speed, we can infer entailment
    label = "entailment"

print(label)
