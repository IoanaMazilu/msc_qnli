new_jobs_premise = 144000
new_jobs_hypothesis = 1/5 * new_jobs_premise

# the hypothesis talks about the proportion of new jobs in the last 12 months, which is not directly mentioned in the premise
# the premise only mentions the number of new jobs created in August, not in the last 12 months
# the hypothesis cannot be entailed from the premise, since the number of jobs in the last 12 months is unknown.
label = "neutral"

print(label)
