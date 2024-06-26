time_premise = 1
time_hypothesis = 2
average_gym_premise = 3
average_gym_hypothesis = 3

# the hypothesis talks about the time period and the average number of gym visits per week, both mentioned in the premise
if time_hypothesis < time_premise:
    # check if the time period in the hypothesis contradicts the time period from the premise
    label = "contradiction"
elif average_gym_hypothesis != average_gym_premise:
    # check if the average number of gym visits per week in the hypothesis contradicts the average number from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
