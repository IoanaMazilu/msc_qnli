# Premise: Dan can do a job alone in 15 hours.
# Hypothesis: Dan can do a job alone in more than 15 hours.
# Golden Label: contradiction

job_time_premise = 15
job_time_hypothesis = 15

# the hypothesis talks about the time Dan takes to do a job alone, which is also mentioned in the premise
if job_time_hypothesis <= job_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact time for the job completion
    # any time higher than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

