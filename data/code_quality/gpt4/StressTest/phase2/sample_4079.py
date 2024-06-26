speed_AB_premise = 40
speed_AB_hypothesis = 30
speed_BC_premise = 60
speed_BC_hypothesis = 60

# the hypothesis refers to the speeds of travel between two sets of cities mentioned in the premise
if speed_AB_hypothesis != speed_AB_premise:
    # check if the speed in the hypothesis from city A to city B contradicts the speed reported in the premise
    label = "contradiction"
elif speed_BC_hypothesis != speed_BC_premise:
    # check if the speed in the hypothesis from city B to city C contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speeds do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
