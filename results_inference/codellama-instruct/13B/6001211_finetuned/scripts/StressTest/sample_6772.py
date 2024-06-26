speed_AB_premise = 50
speed_AB_hypothesis = 40
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis refers to the speeds of travel between cities mentioned in the premise
if speed_AB_hypothesis >= speed_AB_premise:
    # check if the speed of travel from city A to B in the hypothesis contradicts the speed of travel in the premise
    label = "contradiction"
elif speed_BC_hypothesis!= speed_BC_premise:
    # check if the speed of travel from city B to C in the hypothesis contradicts the speed of travel in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of travel from city A to B
    # any speed less than'speed_AB_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)