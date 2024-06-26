y - Ramesh's work time
x - Sushil's work time

work_time_ramesh_premise = 20
work_time_ramesh_hypothesis = 20
work_time_sushil_premise = 25
work_time_sushil_hypothesis = 25

# the hypothesis refers to the work times of Ramesh and Sushil mentioned in the premise
if work_time_ramesh_hypothesis <= work_time_ramesh_premise:
    # check if the estimate of 'work_time_ramesh_hypothesis' contradicts the work time given in the premise
    label = "contradiction"
elif work_time_sushil_hypothesis!= work_time_sushil_premise:
    # check if the work time of Sushil in the hypothesis contradicts the work time given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
