hours_worked_premise = 40
hours_worked_hypothesis = 40
pay_rate_premise = 1
pay_rate_hypothesis = 1

# the hypothesis refers to the number of hours worked per week, which is also mentioned in the premise
if hours_worked_hypothesis >= hours_worked_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked in the premise
    label = "contradiction"
elif pay_rate_hypothesis!= pay_rate_premise:
    # check if the pay rate in the hypothesis contradicts the pay rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
