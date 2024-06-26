yapilab (premise)

work_hours_premise = 40
work_hours_hypothesis = 70
average_orders_premise = 40
average_orders_hypothesis = 40

# the hypothesis talks about the number of hours worked and the average orders per hour, both of which are also mentioned in the premise
if work_hours_hypothesis!= work_hours_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked in the premise
    label = "contradiction"
elif average_orders_hypothesis!= average_orders_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
