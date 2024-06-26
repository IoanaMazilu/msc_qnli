speed_premise = 40
speed_hypothesis = 70

# the hypothesis refers to the driving speed from City A to City B mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the hypothesis that Bob drives at a speed less than'speed_hypothesis'
    label = "contradiction"
else:
    # if the premise speed does not contradict the hypothesis speed, we can infer entailment
    label = "entailment"

print(label)
