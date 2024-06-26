jobs_premise = 5000
jobs_hypothesis = 0.05 * 1000 # 5% of 1000 jobs

# the hypothesis and premise mention the number of jobs Intel will cut in 2014
if jobs_hypothesis > jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # the premise gives only an exact number of jobs
    # any estimate of the percentage of jobs in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
