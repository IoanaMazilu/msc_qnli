hours_per_day_premise = [5, 5, 5, 10, 10]
hours_per_day_hypothesis = [6, 6, 6, 10, 10]

# the hypothesis refers to the number of hours worked per day on specific days, which are also mentioned in the premise
if hours_per_day_hypothesis!= hours_per_day_premise:
    # check if the number of hours worked per day in the hypothesis contradicts the number of hours worked per day in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
