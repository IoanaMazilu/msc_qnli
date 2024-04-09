appearance_ratio_premise = 1/4
appearance_ratio_hypothesis = 2/4

# the hypothesis refers to the ratio of movie lists in which a film must appear, as mentioned in the premise
if appearance_ratio_hypothesis <= appearance_ratio_premise:
    # check if the 'appearance_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
