pay_per_hour_premise = 1
pay_per_hour_hypothesis = 1
max_hours_premise = 10
pay_per_hour_hours_above_max = 1.5

# the hypothesis refers to the pay per hour and the number of hours worked in a week, both mentioned in the premise
if pay_per_hour_hypothesis <= pay_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of 'pay_per_hour_premise'
    label = "contradiction"
elif pay_per_hour_hours_above_max > max_hours_premise:
    # check if the number of hours worked above the maximum in the hypothesis contradicts the maximum number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
