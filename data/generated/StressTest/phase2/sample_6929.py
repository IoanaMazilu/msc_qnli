# Premise: Right now, the ratio between the ages of Sandy and Molly is 4:3.
# Hypothesis: Right now, the ratio between the ages of Sandy and Molly is 5:3.
# Golden Label: contradiction

ratio_sandy_molly_premise = 4/3
ratio_sandy_molly_hypothesis = 5/3

# the hypothesis and premise both talk about the ratio of ages of Sandy and Molly
if ratio_sandy_molly_premise != ratio_sandy_molly_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis is the same as the ratio in the premise, this is an entailment
    label = "entailment"

print(label)

