# Premise: Dan can do a job alone in 12 hours.
# Hypothesis: Dan can do a job alone in more than 12 hours.
# Golden Label: contradiction

job_time_premise = 12
job_time_hypothesis = 12

# the hypothesis refers to the time Dan spends on a job, also mentioned in the premise
if job_time_hypothesis <= job_time_premise:
    # check if the hypothesis value contradicts the time mentioned in the premise
    label = "contradiction"
elif job_time_hypothesis > job_time_premise:
    # the premise specifies a fixed time for the job
    # any time longer than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)

