jobs_premise = 255000
jobless_rate_premise = 4.9
jobs_hypothesis = 255000
jobless_rate_hypothesis = 4.9

# the premise and hypothesis mention the number of jobs added and the jobless rate
if jobs_hypothesis == jobs_premise:
    # if the number of jobs in the hypothesis matches the number of jobs in the premise, we can infer entailment
    label = "entailment"
elif jobs_hypothesis > jobs_premise:
    # if the number of jobs in the hypothesis is greater than the number of jobs in the premise, we can infer entailment
    label = "entailment"
elif jobs_hypothesis < jobs_premise:
    # if the number of jobs in the hypothesis is less than the number of jobs in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the number of jobs in the hypothesis matches the number of jobs in the premise, but the jobless rate in the hypothesis is different from the premise, we can infer neutrality
    label = "neutral"

print(label)
