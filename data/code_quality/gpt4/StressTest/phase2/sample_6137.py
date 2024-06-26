james_hours_worked_premise = 41
james_hours_worked_hypothesis = 41

# the hypothesis refers to the number of hours James worked last week as mentioned in the premise
if james_hours_worked_hypothesis >= james_hours_worked_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
