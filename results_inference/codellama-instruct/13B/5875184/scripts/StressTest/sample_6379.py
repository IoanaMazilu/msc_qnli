premise_hours_per_week = 40
hypothesis_hours_per_week = 30
premise_dollars_per_hour = 10
hypothesis_dollars_per_hour = 1.5

# the hypothesis refers to the number of hours worked and the rate per hour
if hypothesis_hours_per_week <= premise_hours_per_week:
    # check if the estimate of 'hypothesis_hours_per_week' contradicts the number of hours worked in the premise
    label = "contradiction"
elif hypothesis_dollars_per_hour!= premise_dollars_per_hour:
    # check if the rate per hour in the hypothesis contradicts the rate per hour mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
