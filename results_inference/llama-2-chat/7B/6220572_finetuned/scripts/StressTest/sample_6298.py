x_dollars_per_hour_premise = 1
x_dollars_per_hour_hypothesis = 1
hours_worked_premise = 82
hours_worked_hypothesis = 12

# the hypothesis talks about the pay per hour and the number of hours worked, referenced also in the premise
if hours_worked_hypothesis >= hours_worked_premise:
    # check if the estimate of 'hours_worked_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif x_dollars_per_hour_hypothesis!= x_dollars_per_hour_premise:
    # check if the pay per hour in the hypothesis contradicts the pay per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
