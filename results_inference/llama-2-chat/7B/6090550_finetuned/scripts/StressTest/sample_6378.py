hours_worked_premise = 30
hours_worked_hypothesis = 10
wage_rate_premise = 1.5
wage_rate_hypothesis = 1.5

# the hypothesis refers to the number of hours worked and wage rate mentioned in the premise
if hours_worked_hypothesis > hours_worked_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked in the premise
    label = "contradiction"
elif wage_rate_hypothesis!= wage_rate_premise:
    # check if the wage rate in the hypothesis contradicts the wage rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
