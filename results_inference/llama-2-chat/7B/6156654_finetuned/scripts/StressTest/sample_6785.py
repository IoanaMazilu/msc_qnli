# Define variables for the premise and hypothesis
hours_worked_premise = 40
hours_worked_hypothesis = 40
pay_rate_premise = 1
pay_rate_hypothesis = 1.5

# The hypothesis refers to the pay rate for more than 40 hours worked per week
if hours_worked_hypothesis <= hours_worked_premise:
    # Check if the hypothesis contradicts the premise
    label = "contradiction"
elif pay_rate_hypothesis!= pay_rate_premise:
    # Check if the pay rate in the hypothesis contradicts the pay rate in the premise
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
