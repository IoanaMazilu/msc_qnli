jobs_added_premise = 146000
jobless_rate_premise = 7.7
jobless_rate_hypothesis = 7.7

# the hypothesis and premise both mention the jobless rate
if jobless_rate_hypothesis != jobless_rate_premise:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
