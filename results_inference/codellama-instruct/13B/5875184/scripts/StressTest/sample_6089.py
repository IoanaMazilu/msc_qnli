days_worked_premise = 12
days_worked_hypothesis = 72
days_remaining_premise = 10
days_remaining_hypothesis = 10

# the hypothesis refers to the total number of days worked and the remaining work
if days_worked_hypothesis <= days_worked_premise:
    # check if the estimate of 'days_worked_hypothesis' contradicts the number of days worked in the premise
    label = "contradiction"
elif days_remaining_hypothesis!= days_remaining_premise:
    # check if the number of days remaining in the hypothesis contradicts the number of days remaining reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
