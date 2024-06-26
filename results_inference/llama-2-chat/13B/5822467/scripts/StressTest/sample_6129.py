hours_premise = 21
hours_hypothesis = 11
wage_premise = 1.5
wage_hypothesis = 1.5

# the hypothesis refers to the number of hours worked and the wage rate
if hours_hypothesis <= hours_premise:
    # check if the estimate of 'hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif wage_hypothesis!= wage_premise:
    # check if the wage rate in the hypothesis contradicts the wage rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
