job_time_premise = 10
job_time_hypothesis = 30

# the hypothesis refers to the time Annie needs to finish a job, which is also mentioned in the premise
if job_time_hypothesis!= job_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
