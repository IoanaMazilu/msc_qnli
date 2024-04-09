job_time_premise = 15
job_time_hypothesis = 75

# the hypothesis refers to the time Dan needs to do a job alone, also mentioned in the premise
if job_time_hypothesis!= job_time_premise:
    # check if the time estimate in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
