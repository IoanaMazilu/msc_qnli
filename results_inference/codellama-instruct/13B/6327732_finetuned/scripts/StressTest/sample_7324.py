premise_weeks = 2
hypothesis_weeks = 1
premise_times_per_week = 3
hypothesis_times_per_week = 3

# the hypothesis refers to the number of times Rikki goes to the gym and the number of weeks mentioned in the premise
if hypothesis_weeks < premise_weeks:
    # check if the number of weeks in the hypothesis contradicts the estimate of less than 'premise_weeks'
    label = "contradiction"
elif hypothesis_times_per_week!= premise_times_per_week:
    # check if the number of times Rikki goes to the gym in the hypothesis contradicts the number of times mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
