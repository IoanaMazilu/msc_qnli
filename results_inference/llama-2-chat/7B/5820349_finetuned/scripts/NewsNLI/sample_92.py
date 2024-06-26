serious_condition_workers_premise = 4
serious_condition_workers_hypothesis = 4

# the hypothesis mentions the number of wounded staff members in serious condition, which is also referenced in the premise
if serious_condition_workers_hypothesis!= serious_condition_workers_premise:
    # check if the number of wounded staff members in serious condition from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
