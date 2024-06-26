work_days_premise = 5
work_days_hypothesis = 5

# the hypothesis refers to the number of days they work together, which is also mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the exact number of 'work_days_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
