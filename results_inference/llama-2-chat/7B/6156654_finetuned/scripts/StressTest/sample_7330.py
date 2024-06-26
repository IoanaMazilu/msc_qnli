ratio_premise = 3/3/1
ratio_hypothesis = 4/3/1

# the hypothesis refers to the ratio of red, green, and blue toy bricks used in building the tower, as mentioned in the premise
if ratio_hypothesis == ratio_premise:
    # check if the ratio of the hypothesis matches the ratio in the premise
    label = "entailment"
elif ratio_hypothesis!= ratio_premise:
    # check if the ratio of the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer neutral
    label = "neutral"

print(label)
