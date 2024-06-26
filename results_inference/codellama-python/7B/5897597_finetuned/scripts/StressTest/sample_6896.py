walk_days_premise = 3
walk_days_hypothesis = 6

# the hypothesis refers to the number of days Alice walked, mentioned in the premise
if walk_days_hypothesis!= walk_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
