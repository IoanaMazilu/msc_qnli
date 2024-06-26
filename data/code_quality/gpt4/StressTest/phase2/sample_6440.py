shift_hours_premise = 10
shift_hours_hypothesis = 70
shifts_per_week = 4
hourly_order_value = 40

# the hypothesis refers to the number of working hours and the average order value mentioned in the premise
if shift_hours_hypothesis != shift_hours_premise:
    # check if the number of working hours in the hypothesis contradicts the number of working hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
