ramesh_work_duration_premise = 20
ramesh_work_duration_hypothesis = 20
sushil_work_duration_premise = 25
sushil_work_duration_hypothesis = 25

# the hypothesis refers to the time Ramesh and Sushil need to finish a work, mentioned also in the premise
if ramesh_work_duration_hypothesis < ramesh_work_duration_premise:
    # check if the hypothesis value contradicts the premise's claim
    label = "contradiction"
elif sushil_work_duration_hypothesis != sushil_work_duration_premise:
    # check if the number of days Sushil needs in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
