speed_premise = 90
speed_hypothesis = 90
increase_speed_premise = 20
increase_speed_hypothesis = 20

# the hypothesis refers to the same situation as the premise, but with a more specific speed
if speed_hypothesis <= speed_premise:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif increase_speed_hypothesis!= increase_speed_premise:
    # check if the increase in speed in the hypothesis contradicts the increase in speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
