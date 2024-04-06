# Premise: U.S. Adds 255,000 Jobs in July, Jobless Rate at 4.9%.
# Hypothesis: U.S adds 255,000 jobs in July as unemployment rate holds at 4.9 percent.
# Golden Label: entailment

jobs_added_premise = 255000
jobs_added_hypothesis = 255000

unemployment_rate_premise = 4.9
unemployment_rate_hypothesis = 4.9

# the hypothesis and premise both mention the number of jobs added in the U.S in July
# and the unemployment rate for the same period
if jobs_added_hypothesis != jobs_added_premise:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
elif unemployment_rate_hypothesis != unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

