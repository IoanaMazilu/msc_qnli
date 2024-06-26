speed_premise = 30
speed_hypothesis = 20

# the hypothesis refers to the constant speed of Ed while driving from City A to City B, also mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the estimate of'speed_hypothesis' contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
