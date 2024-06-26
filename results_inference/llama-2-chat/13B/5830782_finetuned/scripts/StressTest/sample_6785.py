hours_premise = 40
hours_hypothesis = 40

# the hypothesis refers to the number of hours of work mentioned in the premise
if hours_hypothesis <= hours_premise:
    # check if the hypothesis value contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
