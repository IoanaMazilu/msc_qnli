# Premise: Jobs Report: U.S. Economy Added 321,000 Jobs In November, Unemployment Steady At 5.8%.
# Hypothesis: U.S. Economy Added 321,000 Jobs in November; Unemployment Rate Is 5.8%.
# Golden Label: entailment

jobs_added_premise = 321000
jobs_added_hypothesis = 321000
unemployment_rate_premise = 5.8
unemployment_rate_hypothesis = 5.8

# the hypothesis and premise both mention the number of jobs added in November and the unemployment rate
if jobs_added_premise != jobs_added_hypothesis:
    # check if the number of jobs added in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif unemployment_rate_premise != unemployment_rate_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

