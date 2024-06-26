gym_times_premise = 3
gym_times_hypothesis = 3
weeks_premise = 1
weeks_hypothesis = 5

# the hypothesis refers to the number of times Rikki goes to the gym and the duration of this increase, both mentioned in the premise
if gym_times_premise!= gym_times_hypothesis:
    # check if the number of gym times in the hypothesis contradicts the number of gym times reported in the premise
    label = "contradiction"
elif weeks_premise!= weeks_hypothesis:
    # check if the duration of the gym increase in the hypothesis contradicts the duration of the gym increase reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
