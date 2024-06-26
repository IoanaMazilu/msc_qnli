work_together_days_premise = 10
work_together_days_hypothesis = 10
peter_work_days_premise = 10
peter_work_days_hypothesis = 10

# the hypothesis refers to the duration of joint work and the duration of Peter's work alone
if work_together_days_hypothesis >= work_together_days_premise:
    # check if the duration of joint work in the hypothesis contradicts the duration of joint work in the premise
    label = "contradiction"
elif peter_work_days_hypothesis != peter_work_days_premise:
    # check if the duration of Peter's work in the hypothesis contradicts the duration of Peter's work in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
