second_leg_time_premise = 7
second_leg_time_hypothesis = 6

# the hypothesis refers to the time Henry took to run the second leg of the course, mentioned in the premise
if second_leg_time_premise <= second_leg_time_hypothesis:
    # check if the estimate of'second_leg_time_hypothesis' contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
