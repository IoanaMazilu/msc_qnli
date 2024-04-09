job_time_premise = 10
job_time_hypothesis = 30

# the hypothesis talks about the time it takes Annie to do the job, referenced also in the premise
if job_time_hypothesis >= job_time_premise:
    # check if the hypothesis value contradicts the estimate of 'job_time_premise'
    label = "contradiction"
elif job_time_hypothesis > job_time_premise:
    # the premise gives an estimate for the time it takes Annie to do the job, and the hypothesis value is greater than that estimate
    label = "entailment"
else:
    # if the hypothesis value is equal to the estimate of the premise, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
