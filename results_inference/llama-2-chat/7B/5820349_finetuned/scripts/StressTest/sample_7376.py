shift_hours_premise = 16
shift_hours_hypothesis = 16
average_orders_per_hour_premise = 40
average_orders_per_hour_hypothesis = 40

# the hypothesis refers to the number of hours she worked and the average orders per hour, which are also mentioned in the premise
if shift_hours_hypothesis <= shift_hours_premise:
    # check if the hypothesis value contradicts the number of hours worked in the premise
    label = "contradiction"
elif average_orders_per_hour_hypothesis!= average_orders_per_hour_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
