weeks_premise = 3
weeks_hypothesis = 6
gym_times_premise = 2
gym_times_hypothesis = 2

# the hypothesis refers to the number of weeks and the average gym times per week mentioned in the premise
if weeks_hypothesis < weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the number of weeks reported in the premise
    label = "contradiction"
elif gym_times_hypothesis!= gym_times_premise:
    # check if the average gym times per week in the hypothesis contradicts the average gym times per week reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
