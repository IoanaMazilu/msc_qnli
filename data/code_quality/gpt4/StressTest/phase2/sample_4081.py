ratio_premise = 7/7
ratio_hypothesis = 2/7

# the hypothesis refers to the ratio of distances between A to B and B to C
if ratio_hypothesis > ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # check if the ratio in the hypothesis is less than the ratio given in the premise
    label = "entailment"
else:
    # if the ratio in the hypothesis is equal to the ratio in the premise 
    label = "neutral"

print(label)
