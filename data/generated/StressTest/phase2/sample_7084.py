# Premise: Annie, working alone, can do the same job in just less than 20 hours.
# Hypothesis: Annie, working alone, can do the same job in just 10 hours.
# Golden Label: neutral

job_hours_premise = 20
job_hours_hypothesis = 10

# the hypothesis refers to the number of hours Annie can do the job in, which is also mentioned in the premise
if job_hours_hypothesis >= job_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'job_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'job_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

