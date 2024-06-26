speed_AB_premise = 40
speed_BC_premise = 60
speed_AB_hypothesis = 80
speed_BC_hypothesis = 60

# the hypothesis refers to the speeds of travel between the same cities mentioned in the premise
if speed_AB_hypothesis!= speed_AB_premise:
    # check if the speed of travel from city A to B in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif speed_BC_hypothesis!= speed_BC_premise:
    # check if the speed of travel from city B to C in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speeds do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)