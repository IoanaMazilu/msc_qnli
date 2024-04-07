# Premise: Annie, working alone, can do the same job in just 10 hours.
# Hypothesis: Annie, working alone, can do the same job in just less than 70 hours.
# Golden Label: entailment

job_time_premise = 10
job_time_hypothesis = 70

# the hypothesis refers to the time Annie can finish the job, mentioned also in the premise
if job_time_premise > job_time_hypothesis:
    # check if the estimate of 'job_time_premise' contradicts the maximum time 'job_time_hypothesis' from the hypothesis
    label = "contradiction"
elif job_time_premise < job_time_hypothesis:
    # the premise gives the exact time for the job, which is less than 'job_time_hypothesis'
    # this is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

