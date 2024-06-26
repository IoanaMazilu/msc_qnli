jobs_premise = 533000
years_premise = 34

# the premise mentions the number of jobs lost and the time frame (34 years)

jobs_hypothesis = 533000

# the hypothesis mentions the same number of jobs lost as the premise

if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif years_premise!= jobs_hypothesis:
    # check if the time frame in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same number of jobs lost and the same time frame
    # any comparison of the premise and hypothesis is neutral
    label = "neutral"

print(label)
