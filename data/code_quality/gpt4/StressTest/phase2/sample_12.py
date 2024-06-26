speed_premise = 85
speed_hypothesis = 65

# the hypothesis refers to the speed and the place where John stops which are mentioned in the premise
if speed_premise <= speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis doesn't contradict the speed in the premise, we can infer entailment
    label = "entailment"

print(label)
