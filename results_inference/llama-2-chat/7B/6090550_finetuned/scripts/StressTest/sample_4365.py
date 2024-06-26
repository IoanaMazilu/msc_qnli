 hours_worked_premise = 40
hours_worked_hypothesis = 60
pay_rate_premise = 1
pay_rate_hypothesis = 1

# The hypothesis refers to the number of hours James works per week and his pay rate, both mentioned in the premise
if hours_worked_hypothesis < hours_worked_premise:
    # Check if the number of hours James works per week in the hypothesis contradicts the number of hours he works per week in the premise
    label = "contradiction"
elif pay_rate_hypothesis!= pay_rate_premise:
    # Check if the pay rate in the hypothesis contradicts the pay rate in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

