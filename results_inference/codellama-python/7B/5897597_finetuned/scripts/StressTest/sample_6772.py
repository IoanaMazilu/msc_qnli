speed_AB_premise = 50
speed_AB_hypothesis = 40
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis refers to the speed of travel from city A to B and from B to C mentioned in the premise
if speed_AB_hypothesis >= speed_AB_premise:
    # check if the speed of travel from A to B in the hypothesis contradicts the estimate of less than'speed_AB_premise'
    label = "contradiction"
elif speed_BC_hypothesis!= speed_BC_premise:
    # check if the speed of travel from B to C in the hypothesis contradicts the speed of travel from B to C reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of travel from A to B
    # any speed less than'speed_AB_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
