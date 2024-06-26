speed_A_B_premise = 4
speed_A_B_hypothesis = 7
speed_B_C_premise = 6
speed_B_C_hypothesis = 6

# the hypothesis refers to the traveling speeds between cities mentioned in the premise
if speed_A_B_hypothesis <= speed_A_B_premise:
    # check if the estimate of 'speed_A_B_hypothesis' contradicts the speed from the premise
    label = "contradiction"
elif speed_B_C_hypothesis != speed_B_C_premise:
    # check if the speed between cities B and C in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
