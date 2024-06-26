work_time_ramesh_premise = 60
work_time_ramesh_hypothesis = 20
work_time_sushil_premise = 25
work_time_sushil_hypothesis = 25

# the hypothesis refers to the work time of Ramesh and Sushil mentioned in the premise
if work_time_ramesh_hypothesis >= work_time_ramesh_premise:
    # check if the work time of Ramesh in the hypothesis contradicts the premise
    label = "contradiction"
elif work_time_sushil_hypothesis!= work_time_sushil_premise:
    # check if the work time of Sushil in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
