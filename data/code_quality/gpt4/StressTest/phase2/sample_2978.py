job_time_premise = 10
job_time_hypothesis = 20

# the hypothesis talks about the time Annie takes to do a job alone, which is also mentioned in the premise
if job_time_hypothesis != job_time_premise:
    # check if the time estimate in the hypothesis contradicts the time given in the premise
    label = "contradiction"
else:
    # if the time estimates in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)
