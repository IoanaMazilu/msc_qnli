# Premise: Annie, working alone, can do the same job in just 9 hours.
# Hypothesis: Annie, working alone, can do the same job in just more than 2 hours.
# Golden Label: entailment

job_duration_premise = 9
job_duration_hypothesis = 2

# the hypothesis talks about the job duration, mentioned in the premise
if job_duration_hypothesis >= job_duration_premise:
    # check if the hypothesis value contradicts the 'job_duration_premise'
    label = "contradiction"
else:
    # any job duration less than 'job_duration_premise' is not consistent with the premise
    # so, it can't be explicitly entailed from the premise
    label = "neutral"

print(label)

