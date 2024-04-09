sandy_molly_ratio_premise = 4 / 3
sandy_molly_ratio_hypothesis = 5 / 3

# the hypothesis refers to the age ratio of Sandy and Molly mentioned in the premise
if sandy_molly_ratio_hypothesis!= sandy_molly_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
