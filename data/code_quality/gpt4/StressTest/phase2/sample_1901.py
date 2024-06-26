joint_work_days_premise = 12
joint_work_days_hypothesis = 12
remaining_work_days_premise = 10
remaining_work_days_hypothesis = 10

# the hypothesis refers to the number of days Peter and his colleague worked together, and the number of days Peter worked alone, both mentioned in the premise
if joint_work_days_hypothesis > joint_work_days_premise:
    # check if the estimate of 'joint_work_days_hypothesis' contradicts the number of joint work days in the premise
    label = "contradiction"
elif remaining_work_days_hypothesis != remaining_work_days_premise:
    # check if the number of remaining work days in the hypothesis contradicts the number of remaining work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
