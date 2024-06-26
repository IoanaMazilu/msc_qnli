job_time_premise = 15
job_time_hypothesis = 75

# the hypothesis refers to the time Dan needs to do a job alone, mentioned in the premise
if job_time_hypothesis <= job_time_premise:
    # check if the hypothesis value contradicts the estimate of 'job_time_premise'
    label = "contradiction"
elif job_time_hypothesis > job_time_premise:
    # check if the hypothesis value is greater than the premise value, which means it is not entailed
    label = "neutral"
else:
    # if the hypothesis value is less than or equal to the premise value, it is entailed
    label = "entailment"

print(label)
