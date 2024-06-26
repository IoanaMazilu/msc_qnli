hours_worked_premise = 40
hours_worked_hypothesis = 70
x_per_hour_premise = 1.5 * x_per_hour_hypothesis

# the hypothesis refers to the number of hours worked per week and the pay per hour
if hours_worked_premise >= hours_worked_hypothesis:
    # check if the number of hours worked in the premise contradicts the hypothesis
    label = "contradiction"
elif x_per_hour_premise!= x_per_hour_hypothesis:
    # check if the pay per hour in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
