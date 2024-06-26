shift_hours_premise = 16
shift_hours_hypothesis = 36
avg_orders_premise = 40
avg_orders_hypothesis = 40

# the hypothesis refers to the number of hours Jill worked and the average orders per hour, both mentioned in the premise
if shift_hours_premise >= shift_hours_hypothesis:
    # check if the number of hours Jill worked in the premise contradicts the estimate of less than'shift_hours_hypothesis' hours
    label = "contradiction"
elif avg_orders_premise!= avg_orders_hypothesis:
    # check if the average orders per hour in the premise contradicts the average orders per hour in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
