sandy_molly_ratio_premise = 4/3
sandy_molly_ratio_hypothesis = 5/3

# the hypothesis refers to the ratio between Sandy and Molly's ages, which is also mentioned in the premise
if sandy_molly_ratio_hypothesis!= sandy_molly_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
