james_hours_worked_premise = 45
james_hours_worked_hypothesis = 55

# the hypothesis refers to the number of hours James worked last week, mentioned also in the premise
if james_hours_worked_premise >= james_hours_worked_hypothesis:
    # check if the estimate of 'james_hours_worked_hypothesis' contradicts the number of hours James worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
