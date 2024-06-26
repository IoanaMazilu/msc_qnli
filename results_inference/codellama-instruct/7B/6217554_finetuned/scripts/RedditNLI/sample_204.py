jobs_premise = 5000
jobs_hypothesis = 5

# the hypothesis and premise mention the number of jobs to be cut
if jobs_hypothesis > jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
