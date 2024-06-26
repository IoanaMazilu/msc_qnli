james_work_hours_premise = 41
james_work_hours_hypothesis = 41

# the hypothesis refers to the amount of hours James worked last week, which is also stated in the premise
if james_work_hours_hypothesis > james_work_hours_premise:
    # check if the hypothesis value contradicts the exact number of 'james_work_hours_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
