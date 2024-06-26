speed_premise = 90
speed_hypothesis = 90
increase_speed_premise = 20
increase_speed_hypothesis = 20

# the hypothesis refers to the speed and speed increase mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis speed contradicts the speed reported in the premise
    label = "contradiction"
elif increase_speed_hypothesis!= increase_speed_premise:
    # check if the speed increase in the hypothesis contradicts the speed increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
