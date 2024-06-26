weeks_premise = 3
weeks_hypothesis = 1
gym_times_premise = 2
gym_times_hypothesis = 2

# the hypothesis refers to the number of times Rikki has gone to the gym in a certain number of weeks
if weeks_hypothesis > weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the number of weeks in the premise
    label = "contradiction"
elif gym_times_hypothesis!= gym_times_premise:
    # check if the number of gym times in the hypothesis contradicts the number of gym times in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
