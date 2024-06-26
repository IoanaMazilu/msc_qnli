jobless_claims_premise = 255000
jobless_claims_estimate_premise = 285000
year_premise = 1973

jobless_claims_hypothesis = 255000
year_hypothesis = 1973

# the hypothesis and premise mention the number of jobless claims and the year when this level was last seen
if jobless_claims_premise != jobless_claims_hypothesis or year_premise != year_hypothesis:
    # check if the number of jobless claims or the year in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
