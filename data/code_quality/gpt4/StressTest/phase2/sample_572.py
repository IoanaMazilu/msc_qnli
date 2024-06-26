speed_AB_premise = 40
speed_BC_premise = 60
speed_AB_hypothesis = 60
speed_BC_hypothesis = 60

# the hypothesis refers to Murali's speed of travel between cities mentioned in the premise
if speed_AB_premise != speed_AB_hypothesis:
    # check if the speed of travel from city A to B in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_BC_premise != speed_BC_hypothesis:
    # check if the speed of travel from city B to C in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speeds mentioned in the hypothesis do not contradict those in the premise, we can infer entailment
    label = "entailment"

print(label)
