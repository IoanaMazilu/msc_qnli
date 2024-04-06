# Premise: US economy adds 163K jobs, unemployment rate rises to 8.3%-NYPOST.com.
# Hypothesis: U.S. Adds 163,000 Jobs In July; Unemployment Rate Rises To 8.3%.
# Golden Label: entailment

jobs_added_premise = 163000
jobs_added_hypothesis = 163000
unemployment_rate_premise = 8.3
unemployment_rate_hypothesis = 8.3

# the hypothesis and premise mention the number of jobs added and the unemployment rate
if jobs_added_premise != jobs_added_hypothesis:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
elif unemployment_rate_premise != unemployment_rate_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

