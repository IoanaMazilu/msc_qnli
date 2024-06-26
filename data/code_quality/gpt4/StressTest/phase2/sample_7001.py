ramesh_work_premise = 20
sushil_work_premise = 25
ramesh_work_hypothesis = 20
sushil_work_hypothesis = 25

# the hypothesis refers to the work completion days of Ramesh and Sushil mentioned in the premise
if ramesh_work_hypothesis < ramesh_work_premise:
    # check if the estimate of 'ramesh_work_hypothesis' contradicts the work completion days of Ramesh in the premise
    label = "contradiction"
elif sushil_work_hypothesis != sushil_work_premise:
    # check if the work completion days of Sushil in the hypothesis contradicts the work completion days of Sushil reported in the premise
    label = "contradiction"
else:
    # the premise gives exact work completion days for Ramesh and Sushil
    # the hypothesis statement about Ramesh's work completion days is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
