speed_premise = 10
speed_hypothesis = 90
increase_speed_premise = 20
increase_speed_hypothesis = 20
time_premise = 12
time_hypothesis = 12

# the hypothesis refers to the speed and increase in speed of Xavier at a certain time
if speed_hypothesis < speed_premise:
    # check if the initial speed in the hypothesis contradicts the initial speed in the premise
    label = "contradiction"
elif increase_speed_hypothesis!= increase_speed_premise:
    # check if the increase in speed in the hypothesis contradicts the increase in speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
