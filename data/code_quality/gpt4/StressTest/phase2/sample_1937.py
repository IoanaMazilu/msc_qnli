average_speed_premise = 36
average_speed_hypothesis = 36

# the hypothesis refers to the average speed of the journey mentioned in the premise
if average_speed_hypothesis > average_speed_premise:
    # check if the estimate of 'average_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
