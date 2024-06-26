speed_AB_premise = 4
speed_BC_premise = 6
speed_AB_hypothesis = 1
speed_BC_hypothesis = 6

# the hypothesis speaks about Murali's travel speed between city A to B and B to C, also mentioned in the premise
if speed_AB_hypothesis != speed_AB_premise:
    # check if the speed from city A to B in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed from city B to C in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
