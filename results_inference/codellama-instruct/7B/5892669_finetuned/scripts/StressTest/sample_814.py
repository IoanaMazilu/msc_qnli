speed_AB_premise = 30
speed_AB_hypothesis = 40
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis refers to the speed of travel from city A to city B and from city B to city C mentioned in the premise
if speed_AB_hypothesis <= speed_AB_premise:
    # check if the speed of travel from city A to city B in the hypothesis contradicts the estimate of more than'speed_AB_premise'
    label = "contradiction"
elif speed_BC_hypothesis!= speed_BC_premise:
    # check if the speed of travel from city B to city C in the hypothesis contradicts the speed of travel from city B to city C reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of travel from city A to city B
    # any speed of travel greater than'speed_AB_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
