sandy_molly_ratio_premise = 4/3
sandy_molly_ratio_hypothesis = 5/3

# the hypothesis refers to the ratio of ages of Sandy and Molly mentioned in the premise
if sandy_molly_ratio_hypothesis!= sandy_molly_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
