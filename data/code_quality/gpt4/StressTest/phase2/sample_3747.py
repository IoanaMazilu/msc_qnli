ramesh_work_premise = 20
ramesh_work_hypothesis = 70
sushil_work_premise = 25
sushil_work_hypothesis = 25

# the hypothesis refers to the work completion time of Ramesh and Sushil mentioned in the premise
if ramesh_work_hypothesis > ramesh_work_premise:
    # check if the estimate of 'ramesh_work_hypothesis' contradicts the work completion time of Ramesh in the premise
    label = "contradiction"
elif sushil_work_hypothesis != sushil_work_premise:
    # check if the work completion time of Sushil in the hypothesis contradicts the work completion time of Sushil reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
