jobs_premise = 5000
percentage_workforce_hypothesis = 5

# the hypothesis and premise mention the number of jobs cut by Intel in 2014
if jobs_premise > 0 and jobs_premise < percentage_workforce_hypothesis:
    # check if the number of jobs in the premise contradicts the percentage of workforce in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
