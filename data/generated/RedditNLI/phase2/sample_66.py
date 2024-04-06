# Premise: U.S. Jobless Rate Declines to 7.8%; 114,000 Jobs Added.
# Hypothesis: Unemployment Rate Drops To 7.8 Percent; 114,000 Jobs Added To Payrolls.
# Golden Label: entailment

jobless_rate_premise = 7.8
jobless_rate_hypothesis = 7.8
jobs_added_premise = 114000
jobs_added_hypothesis = 114000

# the hypothesis and premise mention the jobless rate and the number of jobs added
if jobless_rate_premise != jobless_rate_hypothesis:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
elif jobs_added_premise != jobs_added_hypothesis:
    # check if the number of jobs added in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

