hours_per_day_premise = 2
hours_per_day_hypothesis = 9

# the hypothesis refers to the number of hours Mary works per day on Monday, Wednesday and Friday, and Tuesday and Thursday
if hours_per_day_hypothesis <= hours_per_day_premise:
    # check if the estimate of 'hours_per_day_hypothesis' contradicts the number of hours Mary works per day in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
