premise_hours = 4 * 12
premise_orders = 40

hypothesis_hours = 4 * 42
hypothesis_orders = 40

# the hypothesis refers to the number of hours worked and the average orders per hour
if hypothesis_hours > premise_hours:
    # check if the estimate of 'hypothesis_hours' contradicts the number of hours worked in the premise
    label = "contradiction"
elif hypothesis_orders!= premise_orders:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
