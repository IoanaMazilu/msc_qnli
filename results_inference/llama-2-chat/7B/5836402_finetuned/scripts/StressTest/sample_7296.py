river_speed_premise = 2
river_speed_hypothesis = 1

# the hypothesis refers to the speed of the river mentioned in the premise
if river_speed_premise <= river_speed_hypothesis:
    # check if the estimate of 'river_speed_hypothesis' contradicts the speed of the river in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
