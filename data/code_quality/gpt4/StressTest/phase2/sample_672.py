speed_premise = 29
speed_hypothesis = 19

# the hypothesis refers to the driving speed of Jake mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the 'speed_hypothesis' contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
