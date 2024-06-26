ramesh_work_time_premise = 60
ramesh_work_time_hypothesis = 20
sushil_work_time_premise = 25
sushil_work_time_hypothesis = 25

# the hypothesis refers to the work time of Ramesh and Sushil mentioned in the premise
if ramesh_work_time_hypothesis >= ramesh_work_time_premise:
    # check if the estimate of 'ramesh_work_time_hypothesis' contradicts the work time of Ramesh in the premise
    label = "contradiction"
elif sushil_work_time_hypothesis!= sushil_work_time_premise:
    # check if the work time of Sushil in the hypothesis contradicts the work time of Sushil reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the work time of Ramesh
    # any work time less than 'ramesh_work_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
