# Premise: The ratio between the school ages of Neelam and Shaan is more than 4:6 respectively.
# Hypothesis: The ratio between the school ages of Neelam and Shaan is 5:6 respectively.
# Golden Label: neutral

ratio_neelam_shaan_premise = 4/6
ratio_neelam_shaan_hypothesis = 5/6

# the hypothesis refers to the ratio between the school ages of Neelam and Shaan mentioned in the premise
if ratio_neelam_shaan_hypothesis <= ratio_neelam_shaan_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'ratio_neelam_shaan_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_neelam_shaan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

