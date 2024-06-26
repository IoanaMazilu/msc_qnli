increase_week_premise = 1
increase_week_hypothesis = 2

# the hypothesis refers to the increase in the number of gym visits per week, mentioned in the premise
if increase_week_hypothesis >= increase_week_premise:
    # check if the increase in the number of gym visits per week in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the increase in the number of gym visits per week in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
