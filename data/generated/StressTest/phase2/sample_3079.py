# Premise: Dan can do a job alone in less than 82 hours.
# Hypothesis: Dan can do a job alone in 12 hours.
# Golden Label: neutral

job_time_premise = 82
job_time_hypothesis = 12

# the hypothesis talks about the amount of time Dan needs to do a job, referenced also in the premise
if job_time_hypothesis >= job_time_premise:
    # check if the hypothesis time contradicts the estimate of less than 'job_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time needed
    # any time less than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

