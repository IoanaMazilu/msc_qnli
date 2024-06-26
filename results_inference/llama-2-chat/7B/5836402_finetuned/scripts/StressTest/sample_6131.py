dollars_per_hour_premise = 1
dollars_per_hour_hypothesis = 1
hours_worked_premise = 21
hours_worked_hypothesis = 11

# the hypothesis refers to the number of hours worked and the pay per hour mentioned in the premise
if dollars_per_hour_hypothesis!= dollars_per_hour_premise:
    # check if the pay per hour in the hypothesis contradicts the pay per hour reported in the premise
    label = "contradiction"
elif hours_worked_hypothesis!= hours_worked_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
