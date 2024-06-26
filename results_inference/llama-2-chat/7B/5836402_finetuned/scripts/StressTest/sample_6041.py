start_speed_premise = 90
increase_speed_premise = 20
time_premise = 12

start_speed_hypothesis = 90
increase_speed_hypothesis = 20
time_hypothesis = 12

# the hypothesis refers to the initial speed and time intervals mentioned in the premise
if start_speed_hypothesis <= start_speed_premise:
    # check if the estimate of'start_speed_hypothesis' contradicts the initial speed in the premise
    label = "contradiction"
elif increase_speed_hypothesis!= increase_speed_premise:
    # check if the increase in speed in the hypothesis contradicts the increase in speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
