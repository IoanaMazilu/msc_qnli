# Premise: Suresh can complete a job in 15 hours.
# Hypothesis: Suresh can complete a job in more than 15 hours.
# Golden Label: contradiction

job_completion_time_premise = 15
job_completion_time_hypothesis = 15

# the hypothesis talks about the time Suresh takes to complete a job, also referred in the premise
if job_completion_time_hypothesis < job_completion_time_premise:
    # check if the hypothesis value contradicts the given 'job_completion_time_premise'
    label = "contradiction"
elif job_completion_time_hypothesis == job_completion_time_premise:
    # check if the hypothesis value is equal to the premise value
    label = "entailment"
else:
    # the premise gives an exact time for job completion, any time greater than 'job_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

