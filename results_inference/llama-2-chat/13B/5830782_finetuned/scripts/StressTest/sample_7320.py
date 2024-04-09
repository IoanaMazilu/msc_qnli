weeks_premise = 3
weeks_hypothesis = 6
avg_gym_times_premise = 2
avg_gym_times_hypothesis = 2

# the hypothesis refers to the number of weeks and the average gym times mentioned in the premise
if weeks_premise > weeks_hypothesis:
    # check if the number of weeks in the premise contradicts the number of weeks in the hypothesis
    label = "contradiction"
elif avg_gym_times_premise!= avg_gym_times_hypothesis:
    # check if the average gym times in the hypothesis contradicts the average gym times reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
