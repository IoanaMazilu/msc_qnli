ramesh_work_duration_premise = 20
sushil_work_duration_premise = 25
ramesh_work_duration_hypothesis = 50
sushil_work_duration_hypothesis = 25

# the hypothesis refers to the work durations of Ramesh and Sushil mentioned in the premise
if ramesh_work_duration_premise != ramesh_work_duration_hypothesis:
    # check if the duration for Ramesh in the hypothesis contradicts the duration mentioned in the premise
    label = "contradiction"
elif sushil_work_duration_premise != sushil_work_duration_hypothesis:
    # check if the duration for Sushil in the hypothesis contradicts the duration mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
