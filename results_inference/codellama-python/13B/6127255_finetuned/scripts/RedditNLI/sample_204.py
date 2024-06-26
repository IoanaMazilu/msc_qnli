jobs_premise = 5000
jobs_hypothesis = 5000 * 0.05

# the hypothesis and premise mention the number of jobs Intel will cut in 2014
if jobs_hypothesis > jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of jobs to be cut, while the hypothesis gives a percentage of the workforce
    # the percentage of the workforce in the hypothesis is consistent with the number of jobs in the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
