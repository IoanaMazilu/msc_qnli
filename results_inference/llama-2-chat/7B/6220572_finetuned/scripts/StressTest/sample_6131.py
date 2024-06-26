pay_per_hour_premise = 1
pay_per_hour_hypothesis = 1
hours_worked_premise = 21
hours_worked_hypothesis = 11

# the hypothesis talks about the pay per hour and the number of hours worked, referenced also in the premise
if pay_per_hour_hypothesis!= pay_per_hour_premise or hours_worked_hypothesis!= hours_worked_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
