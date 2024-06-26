jobs_gained_premise = 222000
jobs_added_hypothesis = 222000

# the hypothesis and premise mention a number of jobs gained/added in US in June
if jobs_gained_premise != jobs_added_hypothesis:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
