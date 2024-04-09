job_time_premise = 10
job_time_hypothesis = 30

# the hypothesis talks about the time Annie needs to finish a job, which is also mentioned in the premise
if job_time_hypothesis!= job_time_premise:
    # check if the time estimate in the hypothesis contradicts the time estimate in the premise
    label = "contradiction"
else:
    # if the time estimates in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
