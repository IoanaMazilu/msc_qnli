job_time_premise = 15
job_time_hypothesis = 15

# the hypothesis refers to the time Dan needs to do a job alone, which is also mentioned in the premise
if job_time_hypothesis <= job_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
