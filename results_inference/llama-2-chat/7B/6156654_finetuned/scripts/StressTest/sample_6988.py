ratio_premise = 2/3
ratio_hypothesis = 7/3

# the hypothesis refers to the ratio of the ages of Anil and his son at present, as mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the premise
    label = "contradiction"
elif ratio_hypothesis > ratio_premise:
    # check if the ratio in the hypothesis is more than the ratio in the premise
    label = "entailment"
else:
    # if the ratio in the hypothesis is equal to the ratio in the premise, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
