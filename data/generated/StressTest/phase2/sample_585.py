# Premise: The ratio between the school ages of Neelam and Shaan is 5:6 respectively.
# Hypothesis: The ratio between the school ages of Neelam and Shaan is more than 4:6 respectively.
# Golden Label: entailment

ratio_neelam_shaan_premise = 5/6
ratio_neelam_shaan_hypothesis = 4/6

# the hypothesis refers to the ratio between the school ages of Neelam and Shaan mentioned in the premise
if ratio_neelam_shaan_hypothesis >= ratio_neelam_shaan_premise:
    # check if the ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

