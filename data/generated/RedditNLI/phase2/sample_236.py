# Premise: U.S. Jobless Rate Declines to 7.8%; 114,000 Jobs Added.
# Hypothesis: Shocker: Jobless rate falls to 7.8%.
# Golden Label: entailment

jobless_rate_premise = 7.8
jobless_rate_hypothesis = 7.8
jobs_added_premise = 114000

# the hypothesis and premise mention the same jobless rate
if jobless_rate_hypothesis != jobless_rate_premise:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the jobless rate in the hypothesis does not contradict the jobless rate in the premise, we can infer entailment
    # the number of jobs added is not mentioned in the hypothesis, so it does not affect the entailment
    label = "entailment"

print(label)

