pay_per_hour_premise = 1
pay_per_hour_hypothesis = 1
max_hours_premise = 40
max_hours_hypothesis = 40

# the hypothesis refers to the pay per hour and the maximum number of hours worked mentioned in the premise
if pay_per_hour_hypothesis <= pay_per_hour_premise:
    # check if the estimate of 'pay_per_hour_hypothesis' contradicts the pay per hour in the premise
    label = "contradiction"
elif max_hours_hypothesis!= max_hours_premise:
    # check if the maximum number of hours in the hypothesis contradicts the maximum number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
