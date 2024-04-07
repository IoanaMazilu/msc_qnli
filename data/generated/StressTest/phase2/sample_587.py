# Premise: The ratio between the school ages of Neelam and Shaan is 5:6 respectively.
# Hypothesis: The ratio between the school ages of Neelam and Shaan is 7:6 respectively.
# Golden Label: contradiction

neelam_shaan_ratio_premise = 5/6
neelam_shaan_ratio_hypothesis = 7/6

# the hypothesis refers to the ratio between the school ages of Neelam and Shaan mentioned in the premise
if neelam_shaan_ratio_hypothesis != neelam_shaan_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio provided in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio is the same as the premise ratio, we can infer entailment
    label = "entailment"

print(label)

