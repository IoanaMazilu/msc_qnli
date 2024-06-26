sandy_molly_ratio_premise = 4/3
sandy_molly_ratio_hypothesis = 5/3

# the hypothesis refers to the age ratio of Sandy and Molly mentioned in the premise
if sandy_molly_ratio_premise!= sandy_molly_ratio_hypothesis:
    # check if the age ratio in the hypothesis contradicts the age ratio mentioned in the premise
    label = "contradiction"
else:
    # if the age ratio in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
