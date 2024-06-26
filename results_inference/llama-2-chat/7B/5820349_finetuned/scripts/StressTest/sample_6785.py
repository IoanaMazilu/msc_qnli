regular_hours_premise = 40
regular_hours_hypothesis = 40

# the hypothesis refers to the number of regular hours worked by James, mentioned in the premise
if regular_hours_hypothesis <= regular_hours_premise:
    # check if the hypothesis value contradicts the premise value of'regular_hours_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
