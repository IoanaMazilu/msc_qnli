ramesh_work_time_premise = 70
ramesh_work_time_hypothesis = 20
sushil_work_time_premise = 25
sushil_work_time_hypothesis = 25

# the hypothesis refers to the time Ramesh and Sushil need to finish a work, also mentioned in the premise
if ramesh_work_time_hypothesis >= ramesh_work_time_premise:
    # check if the estimate of 'ramesh_work_time_hypothesis' contradicts the premise
    label = "contradiction"
elif sushil_work_time_hypothesis != sushil_work_time_premise:
    # check if the number of days Sushil needs in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives an upper limit for Ramesh's work time,
    # but the exact number of days cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
