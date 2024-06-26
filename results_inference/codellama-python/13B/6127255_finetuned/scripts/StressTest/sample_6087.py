days_together_premise = 12
days_together_hypothesis = 52
days_peter_works_premise = 10
days_peter_works_hypothesis = 10

# the hypothesis refers to the number of days they worked together and the number of days Peter worked, mentioned in the premise
if days_together_hypothesis < days_together_premise:
    # check if the estimate of 'days_together_hypothesis' contradicts the number of days they worked together in the premise
    label = "contradiction"
elif days_peter_works_hypothesis!= days_peter_works_premise:
    # check if the number of days Peter worked in the hypothesis contradicts the number of days Peter worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
