days_worked_premise = 12
days_worked_hypothesis = 52
days_worked_remaining_premise = 10
days_worked_remaining_hypothesis = 10

# the hypothesis refers to the number of days they have worked together and the number of days left to complete the work
if days_worked_premise >= days_worked_hypothesis:
    # check if the estimate of 'days_worked_hypothesis' contradicts the number of days worked in the premise
    label = "contradiction"
elif days_worked_remaining_hypothesis!= days_worked_remaining_premise:
    # check if the number of days left to complete the work in the hypothesis contradicts the number of days left to complete the work reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
