matt_worked_premise = 12
peter_worked_premise = 10
matt_worked_hypothesis = 72
peter_worked_hypothesis = 10

# the hypothesis talks about the total number of days Matt and Peter worked together
if matt_worked_hypothesis <= matt_worked_premise + peter_worked_premise:
    # check if the hypothesis value contradicts the estimate of the total work done in the premise
    label = "contradiction"
elif peter_worked_hypothesis!= peter_worked_premise:
    # check if the number of days Peter worked in the hypothesis contradicts the number of days Peter worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
