shift_hours_premise = 36
shift_hours_hypothesis = 16
average_orders_per_hour_premise = 40
average_orders_per_hour_hypothesis = 40

# The hypothesis refers to the same situation as the premise, but with different shift lengths
if shift_hours_hypothesis!= shift_hours_premise:
    # Check if the number of hours worked in the hypothesis contradicts the number of hours worked in the premise
    label = "contradiction"
elif average_orders_per_hour_hypothesis!= average_orders_per_hour_premise:
    # Check if the average number of orders per hour in the hypothesis contradicts the average number of orders per hour in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
