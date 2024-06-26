jobs_added_premise = 255000
jobs_added_hypothesis = 179000
jobless_rate_premise = 4.9

# the hypothesis refers to the number of jobs added in the U.S. private sector, which is also mentioned in the premise
if jobs_added_hypothesis!= jobs_added_premise:
    # check if the number of jobs added in the private sector in the hypothesis contradicts the number of jobs added in the private sector in the premise
    label = "contradiction"
else:
    # if the number of jobs added in the private sector in the hypothesis does not contradict the number of jobs added in the private sector in the premise, we can infer entailment
    label = "entailment"

print(label)
