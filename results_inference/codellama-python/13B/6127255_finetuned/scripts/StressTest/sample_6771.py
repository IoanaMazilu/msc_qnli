speed_AB_premise = 40
speed_AB_hypothesis = 50
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis refers to the speed of travel between cities A-B and B-C mentioned in the premise
if speed_AB_premise > speed_AB_hypothesis:
    # check if the speed of travel from A to B in the premise contradicts the estimate of less than'speed_AB_hypothesis'
    label = "contradiction"
elif speed_BC_premise!= speed_BC_hypothesis:
    # check if the speed of travel from B to C in the premise contradicts the speed of travel from B to C in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)