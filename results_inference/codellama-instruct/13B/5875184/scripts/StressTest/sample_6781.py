premise_hours_per_week = 80
hypothesis_hours_per_week = 30
premise_dollars_per_hour = x
hypothesis_dollars_per_hour = 2 * premise_dollars_per_hour

# the hypothesis refers to the number of hours worked in a week
if hypothesis_hours_per_week <= premise_hours_per_week:
    # check if the estimate of 'hypothesis_hours_per_week' contradicts the number of hours worked in the premise
    label = "contradiction"
elif hypothesis_dollars_per_hour!= premise_dollars_per_hour:
    # check if the number of dollars per hour in the hypothesis contradicts the number of dollars per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)