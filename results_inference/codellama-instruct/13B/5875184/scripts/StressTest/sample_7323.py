premise_week = 1
hypothesis_week = 2
premise_times_per_week = 3
hypothesis_times_per_week = 3

# the hypothesis refers to the number of times Rikki goes to the gym mentioned in the premise
if hypothesis_week < premise_week:
    # check if the estimate of 'hypothesis_week' contradicts the number of weeks in the premise
    label = "contradiction"
elif hypothesis_times_per_week!= premise_times_per_week:
    # check if the number of times Rikki goes to the gym in the hypothesis contradicts the number of times mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
