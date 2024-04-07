# Premise: Dan can do a job alone in 12 hours.
# Hypothesis: Dan can do a job alone in less than 32 hours.
# Golden Label: entailment

job_time_premise = 12
job_time_hypothesis = 32

# the hypothesis talks about the amount of time Dan can do a job alone, which is also mentioned in the premise
if job_time_premise >= job_time_hypothesis:
    # check if the premise value contradicts the estimate of less than 'job_time_hypothesis'
    label = "contradiction"
elif job_time_premise != job_time_hypothesis:
    # check if the premise value and the hypothesis value are not exactly the same
    label = "neutral"
else:
    # if 'job_time_premise' is less than 'job_time_hypothesis', we can infer entailment
    label = "entailment"

print(label)

