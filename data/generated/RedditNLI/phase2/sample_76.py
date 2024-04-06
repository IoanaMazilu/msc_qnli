# Premise: With unemployment rate dropping to 5.4%, U.S. added 223K jobs in April.
# Hypothesis: U.S. Economy Added 223,000 Jobs in April; Unemployment Rate at 5.4%.
# Golden Label: entailment

unemployment_rate_premise = 5.4
jobs_added_premise = 223000
unemployment_rate_hypothesis = 5.4
jobs_added_hypothesis = 223000

# the hypothesis and premise mention the number of jobs added in April and the unemployment rate 
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

