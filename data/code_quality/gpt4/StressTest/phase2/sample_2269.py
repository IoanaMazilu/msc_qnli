speed_A_B_premise = 20
speed_A_B_hypothesis = 40
speed_B_C_premise = 60
speed_B_C_hypothesis = 60

# the hypothesis refers to the speeds of Murali's travels from city A to city B and from city B to city C
if speed_A_B_hypothesis <= speed_A_B_premise:
    # check if the hypothesis value contradicts the estimate of more than 'speed_A_B_premise' kmph
    label = "contradiction"
elif speed_B_C_hypothesis != speed_B_C_premise:
    # check if the speed from city B to city C in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed from city A to city B,
    # any speed greater than 'speed_A_B_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
