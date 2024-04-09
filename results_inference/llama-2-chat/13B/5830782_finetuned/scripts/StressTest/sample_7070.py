shift_hours_premise = 8
shift_hours_hypothesis = 8
average_orders_premise = 40
average_orders_hypothesis = 40

# the hypothesis refers to the number of shift hours and average orders mentioned in the premise
if shift_hours_hypothesis <= shift_hours_premise:
    # check if the number of shift hours in the hypothesis contradicts the number of shift hours in the premise
    label = "contradiction"
elif average_orders_hypothesis!= average_orders_premise:
    # check if the average orders in the hypothesis contradicts the average orders in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
