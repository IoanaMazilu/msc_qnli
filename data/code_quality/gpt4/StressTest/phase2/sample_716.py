kim_work_time_premise = 3
kim_work_time_hypothesis = 3
david_work_time_premise = 2
david_work_time_hypothesis = 2

# the hypothesis refers to the work time of Kim and David mentioned in the premise
if kim_work_time_hypothesis < kim_work_time_premise:
    # check if the estimate of 'kim_work_time_hypothesis' contradicts the work time of Kim in the premise
    label = "contradiction"
elif david_work_time_hypothesis != david_work_time_premise:
    # check if the work time of David in the hypothesis contradicts the work time of David reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
