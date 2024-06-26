ratio_ages_premise = 4/3
ratio_ages_hypothesis = 4/3

# the hypothesis refers to the ratio of ages of Sandy and Molly mentioned in the premise
if ratio_ages_hypothesis <= ratio_ages_premise:
    # check if the hypothesis value contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
