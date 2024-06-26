jobs_added_premise = 222000
jobs_added_hypothesis = 222000

# the hypothesis and premise mention the number of jobs added in the U.S. in June
if jobs_added_hypothesis != jobs_added_premise:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)