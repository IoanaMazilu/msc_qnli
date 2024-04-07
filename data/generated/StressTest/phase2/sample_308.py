# Premise: Right now, the ratio between the ages of Sandy and Molly is 4:3.
# Hypothesis: Right now, the ratio between the ages of Sandy and Molly is less than 4:3.
# Golden Label: contradiction

ratio_ages_premise = 4 / 3
ratio_ages_hypothesis = 4 / 3

# the hypothesis refers to the ratio between the ages of Sandy and Molly, mentioned also in the premise
if ratio_ages_hypothesis >= ratio_ages_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif ratio_ages_hypothesis == ratio_ages_premise:
    # check if the hypothesis value is exactly the same as the premise value
    label = "entailment"
else:
    # if the hypothesis ratio is less than the premise ratio, it does not contradict it but it also can't be explicitly entailed from the premise
    label = "neutral"

print(label)

