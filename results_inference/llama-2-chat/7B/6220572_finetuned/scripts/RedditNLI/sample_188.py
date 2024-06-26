jobs_premise = 255000
jobs_hypothesis = 179000

# the hypothesis and premise mention the number of jobs added in the US
# the premise gives the total number of jobs added, while the hypothesis gives the number of private sector jobs added
if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
