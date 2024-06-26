work_hours_premise = 10
work_hours_hypothesis = 10

# the hypothesis refers to the same job Annie can do alone, specified also in the premise
if work_hours_hypothesis >= work_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_hours_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
