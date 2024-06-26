job_pay_premise = 150
job_pay_hypothesis = 150

# the hypothesis talks about the pay of Lexi's job, referenced also in the premise
if job_pay_hypothesis >= job_pay_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_pay_premise'
    label = "contradiction"
else:
    # the premise gives an exact value for the pay
    # any pay less than 'job_pay_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
