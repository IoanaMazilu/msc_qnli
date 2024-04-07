# Premise: Dan can do a job alone in 15 hours.
# Hypothesis: Dan can do a job alone in less than 25 hours.
# Golden Label: entailment

job_time_premise = 15
job_time_hypothesis = 25

# the hypothesis talks about the time Dan can do a job alone, which is also referenced in the premise
if job_time_hypothesis < job_time_premise:
    # check if the hypothesis value contradicts the exact number 'job_time_premise' in the premise
    label = "contradiction"
elif job_time_hypothesis == job_time_premise:
    # check if the hypothesis value is equal to the premise value
    label = "entailment"
else:
    # the premise gives an exact time for Dan to do the job
    # any time less than 'job_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

