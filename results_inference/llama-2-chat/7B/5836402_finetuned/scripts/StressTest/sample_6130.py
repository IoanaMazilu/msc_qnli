hours_worked_premise = 11
hours_worked_hypothesis = 21
x_dollars_per_hour_premise = 1.5
x_dollars_per_hour_hypothesis = 1.5

# the hypothesis refers to the number of hours worked and the pay per hour mentioned in the premise
if hours_worked_hypothesis <= hours_worked_premise:
    # check if the hypothesis value contradicts the estimate of more than 'hours_worked_premise'
    label = "contradiction"
elif x_dollars_per_hour_hypothesis!= x_dollars_per_hour_premise:
    # check if the pay per hour in the hypothesis contradicts the pay per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
