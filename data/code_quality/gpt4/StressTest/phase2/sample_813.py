speed_AB_premise = 40
speed_AB_hypothesis = 30
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis refers to the speed of travel between cities A-B and B-C mentioned in the premise
if speed_AB_premise <= speed_AB_hypothesis:
    # check if the estimate of 'speed_AB_hypothesis' contradicts the speed between city A-B in the premise
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed between city B-C in the hypothesis contradicts the speed of travel between city B-C reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
