job_time_premise = 70
job_time_hypothesis = 20

# the hypothesis refers to the time James takes to finish a job mentioned in the premise
if job_time_hypothesis >= job_time_premise:
    # check if the estimate of 'job_time_hypothesis' contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
