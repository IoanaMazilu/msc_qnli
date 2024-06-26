hours_premise = 12
hours_hypothesis = 82

# the hypothesis refers to the number of hours Harry works, which is also mentioned in the premise
if hours_hypothesis < hours_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the number of hours in the hypothesis does not contradict the number of hours in the premise, we can infer entailment
    label = "entailment"

print(label)
