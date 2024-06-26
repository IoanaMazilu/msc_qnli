old_ratio_premise = 5/3
old_ratio_hypothesis = 7/3

# the hypothesis refers to the age ratio between 'he' and Tom mentioned in the premise
if old_ratio_hypothesis <= old_ratio_premise:
    # check if the hypothesis value contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
