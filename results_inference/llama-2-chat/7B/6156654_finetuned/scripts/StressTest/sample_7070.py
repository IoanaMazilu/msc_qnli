hours_worked_premise = 8
hours_worked_hypothesis = 8
average_orders_premise = 40
average_orders_hypothesis = 40

# The hypothesis talks about the number of hours Jill worked and the average orders per hour, which are also mentioned in the premise
if hours_worked_hypothesis!= hours_worked_premise:
    # Check if the number of hours worked in the hypothesis contradicts the number of hours worked in the premise
    label = "contradiction"
elif average_orders_hypothesis!= average_orders_premise:
    # Check if the average orders per hour in the hypothesis contradicts the average orders per hour in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
