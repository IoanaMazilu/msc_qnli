# Premise: He works at it for 20 days and then Rajesh finished it in 30 days.
# Hypothesis: He works at it for less than 80 days and then Rajesh finished it in 30 days.
# Golden Label: entailment

days_worked_premise = 20
days_worked_hypothesis = 80
days_rajesh_finished_premise = 30
days_rajesh_finished_hypothesis = 30

# the hypothesis talks about the number of days he worked and Rajesh finished, which are also referenced in the premise
if days_worked_premise >= days_worked_hypothesis:
    # check if the estimate of 'days_worked_hypothesis' contradicts the number of worked days in the premise
    label = "contradiction"
elif days_rajesh_finished_hypothesis != days_rajesh_finished_premise:
    # check if the number of days Rajesh finished in the hypothesis contradicts the number of days Rajesh finished reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

