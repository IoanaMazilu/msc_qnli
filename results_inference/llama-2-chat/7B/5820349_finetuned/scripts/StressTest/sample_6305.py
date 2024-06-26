james_work_hours_premise = 41
james_work_hours_hypothesis = 61

# the hypothesis refers to the number of hours James worked last week, mentioned in the premise
if james_work_hours_hypothesis!= james_work_hours_premise:
    # check if the number of hours James worked in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
