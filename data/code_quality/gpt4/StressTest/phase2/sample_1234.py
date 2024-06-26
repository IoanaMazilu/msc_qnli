speed_AB_premise = 10
speed_AB_hypothesis = 40
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis talks about the speeds of Murali's travels from A to B and from B to C, which are also mentioned in the premise
if speed_AB_hypothesis <= speed_AB_premise:
    # check if the speed from A to B in the hypothesis contradicts the premise estimate of more than 'speed_AB_premise' kmph
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed from B to C in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # for the route from A to B, the premise gives only an estimate of more than 'speed_AB_premise' kmph
    # any speed greater than 'speed_AB_premise' kmph is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
