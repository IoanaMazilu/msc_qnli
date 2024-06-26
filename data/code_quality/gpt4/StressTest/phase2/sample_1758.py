joint_work_days_premise = 12
joint_work_days_hypothesis = 82
peter_work_days_premise = 10
peter_work_days_hypothesis = 10

# the hypothesis refers to the number of days Matt and Peter worked together and the remaining days Peter worked alone
if joint_work_days_hypothesis < joint_work_days_premise or peter_work_days_hypothesis != peter_work_days_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif joint_work_days_hypothesis > joint_work_days_premise:
    # check if the estimate of 'joint_work_days_hypothesis' contradicts the number of joint work days in the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
