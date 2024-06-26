jobless_rate_premise = 7.8
jobs_added_premise = 114000

# the premise gives the actual jobless rate and number of jobs added
if jobless_rate_premise == jobless_rate_hypothesis and jobs_added_premise == jobs_added_hypothesis:
    # if the premise and hypothesis values match, we can infer entailment
    label = "entailment"
else:
    # if the premise and hypothesis values do not match, we can infer contradiction or neutrality
    if jobless_rate_hypothesis < jobless_rate_premise or jobs_added_hypothesis < jobs_added_premise:
        label = "contradiction"
    else:
        label = "neutral"

print(label)
