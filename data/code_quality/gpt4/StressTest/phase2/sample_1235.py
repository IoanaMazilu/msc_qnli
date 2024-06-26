speed_AB_premise = 40
speed_AB_hypothesis = 10
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis refers to the speed of travel from city A to city B and from city B to city C mentioned in the premise
if speed_AB_premise != speed_AB_hypothesis:
    # check if the speed of travel from city A to city B in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif speed_BC_premise != speed_BC_hypothesis:
    # check if the speed of travel from city B to city C in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speeds do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
