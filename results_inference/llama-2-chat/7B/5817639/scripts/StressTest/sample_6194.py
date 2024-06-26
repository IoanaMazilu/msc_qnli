job_pay_premise = 150
job_pay_hypothesis = 0

# the hypothesis talks about the pay of a job, which is also mentioned in the premise
if job_pay_hypothesis <= job_pay_premise:
    # check if the hypothesis value contradicts the estimate of 'job_pay_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the pay of the job
    # any pay less than 'job_pay_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
