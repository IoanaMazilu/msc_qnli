# Premise: The ratio between the school ages of Neelam and Shaan is 5:6 respectively.
# Hypothesis: The ratio between the school ages of Neelam and Shaan is more than 3:6 respectively.
# Golden Label: entailment

neelam_shaan_ratio_premise = 5 / 6
neelam_shaan_ratio_hypothesis = 3 / 6

# the hypothesis refers to the ratio of school ages between Neelam and Shaan, which is also stated in the premise
if neelam_shaan_ratio_hypothesis >= neelam_shaan_ratio_premise:
    # check if the hypothesis ratio contradicts the ratio stated in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)

