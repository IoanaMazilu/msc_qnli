# Premise: Suresh can complete a job in less than 25 hours.
# Hypothesis: Suresh can complete a job in 15 hours.
# Golden Label: neutral

job_completion_premise = 25
job_completion_hypothesis = 15

# the hypothesis talks about the time Suresh takes to complete a job, referenced also in the premise
if job_completion_hypothesis >= job_completion_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_completion_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Suresh takes to complete a job
    # any time less than 'job_completion_premise' hours is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

