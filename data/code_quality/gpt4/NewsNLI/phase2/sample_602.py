critical_condition_premise = 1
fair_condition_premise = 1
critical_condition_hypothesis = 1

# the hypothesis mentions the number of firefighters in critical condition, which is also referenced in the premise
# however, the hypothesis does not mention the firefighter in fair condition
if critical_condition_hypothesis > critical_condition_premise:
    # check if the number of critical conditions in the hypothesis contradicts the number of critical conditions in the premise
    label = "contradiction"
else:
    # if the number of critical conditions in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
