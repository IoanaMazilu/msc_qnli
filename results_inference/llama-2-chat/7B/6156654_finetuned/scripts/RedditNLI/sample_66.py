jobless_rate_premise = 7.8
jobs_added_premise = 114000
jobless_rate_hypothesis = 7.8
jobs_added_hypothesis = 114000

# the hypothesis mentions the same values for jobless rate and jobs added as in the premise
if jobless_rate_premise!= jobless_rate_hypothesis:
    # check if the jobless rate in the hypothesis contradicts the jobless rate reported in the premise
    label = "contradiction"
elif jobs_added_premise!= jobs_added_hypothesis:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
