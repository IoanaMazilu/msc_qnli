 hours_worked_premise = 40
hours_worked_hypothesis = 40
pay_rate_premise = 1
pay_rate_hypothesis = 1

# the hypothesis talks about the number of hours worked, and the pay rate, both mentioned in the premise
if hours_worked_premise >= hours_worked_hypothesis:
    # check if the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
elif pay_rate_premise!= pay_rate_hypothesis:
    # check if the pay rate in the hypothesis contradicts the pay rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
