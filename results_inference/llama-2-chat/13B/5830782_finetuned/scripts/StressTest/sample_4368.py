james_hours_worked_premise = 41
james_hours_worked_hypothesis = 51

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if james_hours_worked_premise >= james_hours_worked_hypothesis:
    # check if the number of hours James worked in the premise contradicts the hypothesis that he worked less than 'james_hours_worked_hypothesis' hours
    label = "contradiction"
else:
    # if the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
