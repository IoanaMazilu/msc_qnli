# Premise: Dan can do a job alone in 12 hours.
# Hypothesis: Dan can do a job alone in less than 82 hours.
# Golden Label: entailment

job_time_premise = 12
job_time_hypothesis = 82

# the hypothesis refers to the time it takes for Dan to do a job alone, which is also mentioned in the premise
if job_time_hypothesis < job_time_premise:
    # check if the 'job_time_hypothesis' contradicts 'job_time_premise'
    label = "contradiction"
elif job_time_hypothesis >= job_time_premise:
    # the premise explicitly states the time it takes for Dan to do the job alone
    # any time longer than or equal to 'job_time_premise' can be entailed from the premise
    label = "entailment"

print(label)

