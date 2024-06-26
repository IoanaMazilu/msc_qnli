number_jobs_premise = 255000
number_jobs_hypothesis = 179000

# the hypothesis and premise mention the number of jobs in the U.S. private sector
if number_jobs_hypothesis!= number_jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
