jobs_premise = 255000
jobs_hypothesis = 179000

# the premise gives the total number of jobs added in the U.S. in July
if jobs_hypothesis!= jobs_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis value contradicts the premise value, we can infer entailment
    label = "entailment"

print(label)
