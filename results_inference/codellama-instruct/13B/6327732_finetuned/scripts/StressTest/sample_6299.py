hours_per_week_premise = 12
hours_per_week_hypothesis = 52
hourly_wage_premise = x
hourly_wage_hypothesis = 1.5 * hourly_wage_premise

# the hypothesis refers to the number of hours worked and the hourly wage, both mentioned in the premise
if hours_per_week_hypothesis <= hours_per_week_premise:
    # check if the estimate of 'hours_per_week_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif hourly_wage_hypothesis!= hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
