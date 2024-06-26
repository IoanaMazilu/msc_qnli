days_matt_worked_premise = 12
days_matt_worked_hypothesis = 52
days_peter_worked_hypothesis = 10

# the hypothesis refers to the number of days Matt worked and the number of days Peter worked, which are also mentioned in the premise
if days_matt_worked_hypothesis >= days_matt_worked_premise:
    # check if the estimate of 'days_matt_worked_hypothesis' contradicts the number of days Matt worked in the premise
    label = "contradiction"
elif days_peter_worked_hypothesis!= days_peter_worked_premise:
    # check if the number of days Peter worked in the hypothesis contradicts the number of days Peter worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
