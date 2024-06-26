days_worked_premise = 40
days_worked_hypothesis = 20
days_finished_premise = 30
days_finished_hypothesis = 30

# the hypothesis refers to the number of days worked and finished, mentioned in the premise
if days_worked_hypothesis >= days_worked_premise:
    # check if the estimate of 'days_worked_hypothesis' contradicts the number of days worked in the premise
    label = "contradiction"
elif days_finished_hypothesis!= days_finished_premise:
    # check if the number of days finished in the hypothesis contradicts the number of days finished reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
