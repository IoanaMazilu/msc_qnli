james_work_hours_premise = 42
james_work_hours_hypothesis = 42

# the hypothesis refers to the number of hours James worked in the same week
if james_work_hours_hypothesis >= james_work_hours_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
