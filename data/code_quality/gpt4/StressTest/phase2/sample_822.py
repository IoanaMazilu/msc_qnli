max_hours_work_premise = 70
max_hours_work_hypothesis = 60

# the hypothesis refers to the maximum number of hours Mary works in a restaurant, which is also mentioned in the premise
if max_hours_work_hypothesis >= max_hours_work_premise:
    # check if the hypothesis estimate contradicts the maximum hours in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, it can be inferred as entailment
    # as it is exactly in line with the premise
    label = "entailment"

print(label)
