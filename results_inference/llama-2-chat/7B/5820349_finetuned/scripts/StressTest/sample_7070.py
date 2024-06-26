shift_hours_premise = 8
shift_hours_hypothesis = 8 + 2
average_orders_per_hour = 40

# the hypothesis refers to the number of hours Jill worked and the average orders per hour, both mentioned in the premise
if shift_hours_hypothesis!= shift_hours_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
