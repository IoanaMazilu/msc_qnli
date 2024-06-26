ratio_neelam_shaan_premise = 5/6
ratio_neelam_shaan_hypothesis = 3/6

# The hypothesis refers to the ratio of school ages of Neelam and Shaan, which is also mentioned in the premise
if ratio_neelam_shaan_hypothesis != ratio_neelam_shaan_premise:
    # Check if the ratio of school ages in the hypothesis contradicts the ratio of school ages in the premise
    label = "contradiction"
else:
    # If the ratio of school ages in the hypothesis does not contradict the ratio of school ages in the premise, we can infer entailment
    label = "entailment"

print(label)
