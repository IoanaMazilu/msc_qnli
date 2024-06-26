work_days_premise = 20
work_days_hypothesis = 20

# the hypothesis refers to the same work duration as the premise
if work_days_hypothesis < work_days_premise:
    # check if the hypothesis value contradicts the exact work duration in the premise
    label = "contradiction"
elif work_days_hypothesis > work_days_premise:
    # check if the hypothesis value contradicts the exact work duration in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
