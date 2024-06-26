ratio_premise = 4/3/1
ratio_hypothesis = 4/3/1

# the hypothesis refers to the ratio of red, green and blue toy bricks used in building the tower, which is also mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif ratio_hypothesis < ratio_premise:
    # check if the ratio in the hypothesis is less than the ratio in the premise
    # this is entailed by the premise
    label = "entailment"
else:
    # if the ratio in the hypothesis is equal to the ratio in the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
