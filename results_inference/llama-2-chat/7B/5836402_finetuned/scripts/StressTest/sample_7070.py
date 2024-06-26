worked_hours_premise = 2
worked_hours_hypothesis = 2
average_orders_premise = 40
average_orders_hypothesis = 40

# the hypothesis refers to the number of worked hours and the average orders per hour mentioned in the premise
if worked_hours_hypothesis!= worked_hours_premise:
    # check if the number of worked hours in the hypothesis contradicts the number of worked hours reported in the premise
    label = "contradiction"
elif average_orders_hypothesis!= average_orders_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
