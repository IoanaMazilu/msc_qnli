average_speed_premise = 60
average_speed_hypothesis = 70

# the hypothesis refers to the average speed of Ganesh from X to Y, also mentioned in the premise
if average_speed_premise != average_speed_hypothesis:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis average speed does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
