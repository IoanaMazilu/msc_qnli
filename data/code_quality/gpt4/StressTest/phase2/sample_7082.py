job_duration_premise = 15
job_duration_hypothesis = 75

# the hypothesis talks about the duration Dan needs to complete a job, referenced also in the premise
if job_duration_hypothesis != job_duration_premise:
    # check if the hypothesis value contradicts the 'job_duration_premise'
    label = "contradiction"
else:
    # if the hypothesis duration is the same as the one in the premise, we can infer entailment
    label = "entailment"

print(label)
