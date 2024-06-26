james_hours_worked_premise = 41
james_hours_worked_hypothesis = 71

# the hypothesis refers to the number of hours James worked last week, mentioned also in the premise
if james_hours_worked_premise >= james_hours_worked_hypothesis:
    # check if the number of hours James worked in the premise contradicts the estimate of less than 'james_hours_worked_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
