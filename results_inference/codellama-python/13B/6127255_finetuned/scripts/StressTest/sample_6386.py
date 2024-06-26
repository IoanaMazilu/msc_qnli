james_hours_worked_premise = 45
james_hours_worked_hypothesis = 35

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if james_hours_worked_hypothesis!= james_hours_worked_premise:
    # check if the number of hours James worked last week in the hypothesis contradicts the number of hours James worked last week in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
