# define the ratios in premise and hypothesis
ratio_premise = 2 / 5
ratio_hypothesis = 2 / 5

# the hypothesis refers to the ratio of distances from A to B and B to C mentioned in the premise
if ratio_hypothesis != ratio_premise:
    # if the ratio in the hypothesis is not equal to the ratio in the premise, we have a contradiction
    label = "contradiction"
elif ratio_hypothesis == ratio_premise:
    # if the ratio in the hypothesis is equal to the ratio in the premise, we have entailment
    label = "entailment"
else:
    # if neither contradiction nor entailment can be determined, the relation is neutral
    label = "neutral"

print(label)
