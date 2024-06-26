job_time_premise = 10
job_time_hypothesis = 30

# the hypothesis talks about the time Annie needs to do a job, referenced also in the premise
if job_time_hypothesis!= job_time_premise:
    # check if the time Annie needs to do the job in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
