work_days_premise = 9
work_days_hypothesis = 9

# the hypothesis refers to the number of days he worked alone before being joined by Sandra
if work_days_hypothesis != work_days_premise:
    # check if the hypothesis value contradicts the premise one
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
