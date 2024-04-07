# Premise: Dan can do a job alone in less than 25 hours.
# Hypothesis: Dan can do a job alone in 15 hours.
# Golden Label: neutral

job_hours_premise = 25
job_hours_hypothesis = 15

# the hypothesis mentions the number of hours Dan can do a job alone, also referenced in the premise
if job_hours_hypothesis >= job_hours_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'job_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'job_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

