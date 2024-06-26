workers_condition_premise = 4
workers_condition_hypothesis = 4

# the hypothesis mentions the number of staff members in serious condition, which is also referenced in the premise
if workers_condition_hypothesis != workers_condition_premise:
    # check if the number of workers in serious condition in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis numbers do not contradict the premise numbers, we can infer entailment
    label = "entailment"

print(label)
