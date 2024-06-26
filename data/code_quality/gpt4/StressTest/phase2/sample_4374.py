avg_speed_premise = 54
avg_speed_hypothesis = 44

# the hypothesis refers to the average speed of Ganesh from X to Y, mentioned in the premise
if avg_speed_premise <= avg_speed_hypothesis:
    # check if the 'avg_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
else:
    # if the speed value in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
