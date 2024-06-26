number_jobs_premise = 5000
number_jobs_hypothesis = 50

# the hypothesis and premise mention the number of jobs cut by Intel
if number_jobs_hypothesis > number_jobs_premise:
    # check if the number of jobs cut in the hypothesis is greater than the number of jobs cut in the premise
    label = "contradiction"
else:
    # if the number of jobs cut in the hypothesis is less than or equal to the number of jobs cut in the premise, we can infer entailment
    label = "entailment"

print(label)
