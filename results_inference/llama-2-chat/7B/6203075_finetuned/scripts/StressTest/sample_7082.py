job_time_premise = 15
job_time_hypothesis = 75

# the hypothesis talks about the time Dan needs to do a job alone, referenced also in the premise
if job_time_hypothesis!= job_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the time in the hypothesis does not contradict the time in the premise, we can infer entailment
    label = "entailment"

print(label)
