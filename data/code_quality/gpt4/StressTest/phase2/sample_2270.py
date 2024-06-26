speed_AB_premise = 40
speed_AB_hypothesis = 80
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis refers to the speed of travel between cities A-B and B-C mentioned in the premise
if speed_AB_premise != speed_AB_hypothesis:
    # check if the speed of travel between cities A-B in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed of travel between cities B-C in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
