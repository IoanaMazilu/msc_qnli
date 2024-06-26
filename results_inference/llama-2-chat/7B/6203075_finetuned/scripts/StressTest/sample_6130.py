hours_worked_premise = 11
hours_worked_hypothesis = 21
pay_rate_premise = 1.5
pay_rate_hypothesis = 1.5

# the hypothesis refers to the hours worked and pay rate mentioned in the premise
if hours_worked_hypothesis <= hours_worked_premise:
    # check if the 'hours_worked_hypothesis' contradicts the premise
    label = "contradiction"
elif pay_rate_hypothesis!= pay_rate_premise:
    # check if the pay rate in the hypothesis contradicts the pay rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
