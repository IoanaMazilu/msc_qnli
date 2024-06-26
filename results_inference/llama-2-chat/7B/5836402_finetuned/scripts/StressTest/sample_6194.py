job_pay_per_day_premise = 150
job_pay_per_day_hypothesis = 150

# the hypothesis refers to the job pay per day mentioned in the premise
if job_pay_per_day_hypothesis >= job_pay_per_day_premise:
    # check if the estimate of 'job_pay_per_day_hypothesis' contradicts the number of job pay per day in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
