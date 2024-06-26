jobs_added_premise = 255000
jobs_added_hypothesis = 255000
jobless_rate_premise = 4.9
jobless_rate_hypothesis = 4.9

# the hypothesis and premise mention the number of jobs added and the jobless rate in July
if jobs_added_hypothesis!= jobs_added_premise:
    # check if the number of jobs added in the hypothesis contradicts the number of jobs added in the premise
    label = "contradiction"
elif jobless_rate_hypothesis!= jobless_rate_premise:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
