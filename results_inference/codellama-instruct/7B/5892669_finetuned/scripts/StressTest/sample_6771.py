speed_AB_premise = 40
speed_BC_premise = 60
speed_AB_hypothesis = 50
speed_BC_hypothesis = 60

# the hypothesis refers to the speed of travel from city A to B and from B to C mentioned in the premise
if speed_AB_premise >= speed_AB_hypothesis:
    # check if the estimate of'speed_AB_hypothesis' contradicts the speed of travel from A to B in the premise
    label = "contradiction"
elif speed_BC_hypothesis!= speed_BC_premise:
    # check if the speed of travel from B to C in the hypothesis contradicts the speed of travel from B to C reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
