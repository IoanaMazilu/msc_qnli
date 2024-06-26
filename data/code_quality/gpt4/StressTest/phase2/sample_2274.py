job_completion_time_premise = 15
job_completion_time_hypothesis = 45

# the hypothesis refers to the job completion time of Suresh mentioned in the premise
if job_completion_time_hypothesis < job_completion_time_premise:
    # check if the hypothesis value contradicts the job completion time mentioned in the premise
    label = "contradiction"
elif job_completion_time_hypothesis == job_completion_time_premise:
    # if the job completion time in the hypothesis is equal to the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is more than the premise but doesn't contradict it, it is neutral
    label = "neutral"

print(label)
