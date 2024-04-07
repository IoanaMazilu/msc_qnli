# Premise: Dan can do a job alone in less than 32 hours.
# Hypothesis: Dan can do a job alone in 12 hours.
# Golden Label: neutral

job_time_premise = 32
job_time_hypothesis = 12

# the hypothesis refers to the time Dan takes to do a job alone, which is also mentioned in the premise
if job_time_hypothesis >= job_time_premise:
    # check if the time the hypothesis says Dan takes contradicts the premise of less than 'job_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Dan takes
    # any time less than 'job_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

