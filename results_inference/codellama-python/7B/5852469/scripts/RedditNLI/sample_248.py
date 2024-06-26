number_jobs_premise = 100000
number_jobs_hypothesis = 100000

# the hypothesis and premise mention the same number of jobs
if number_jobs_premise!= number_jobs_hypothesis:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same number of jobs
    # any estimate of the number of jobs in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
