# Premise: Economy Adds 192,000 Jobs in March, Unemployment Rate Unchanged.
# Hypothesis: U.S. creates 192,000 jobs in March.
# Golden Label: neutral

jobs_added_premise = 192000
jobs_added_hypothesis = 192000

# the hypothesis and premise mention the number of jobs added in March
if jobs_added_hypothesis != jobs_added_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

