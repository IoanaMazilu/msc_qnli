weeks_premise = 1
weeks_hypothesis = 5
gym_times_premise = 3
gym_times_hypothesis = 3

# the hypothesis refers to the number of weeks and the average gym times mentioned in the premise
if weeks_hypothesis!= weeks_premise + 1:
    # check if the number of weeks in the hypothesis contradicts the number of weeks reported in the premise
    label = "contradiction"
elif gym_times_hypothesis!= gym_times_premise:
    # check if the average gym times in the hypothesis contradicts the average gym times reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
