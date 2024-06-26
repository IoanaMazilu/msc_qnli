job_time_premise = 15
job_time_hypothesis = 15

# the hypothesis refers to the time Dan can do a job alone, which is also mentioned in the premise
if job_time_hypothesis >= job_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif job_time_hypothesis < job_time_premise:
    # if the hypothesis value is less than the premise value, it does not contradict it
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
