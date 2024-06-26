speed_premise = 60
speed_hypothesis = 30

# the hypothesis refers to the driving speed from town Q to B mentioned in the premise
if speed_premise < speed_hypothesis:
    # check if the speed of 'speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
