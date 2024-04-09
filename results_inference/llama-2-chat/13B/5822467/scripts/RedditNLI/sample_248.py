jobs_premise = 67000

# the hypothesis and premise mention the number of jobs gained
if jobs_premise!= jobs_hypothesis:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the number of jobs in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
