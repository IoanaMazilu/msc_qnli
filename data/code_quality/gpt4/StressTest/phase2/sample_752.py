red_green_blue_ratio_premise = [4, 3, 1]
red_green_blue_ratio_hypothesis = [4, 3, 1]

# The hypothesis refers to the ratio of red, green, and blue toy bricks used by Tali to build a tower, which is also mentioned in the premise.
if red_green_blue_ratio_hypothesis >= red_green_blue_ratio_premise:
    # Check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # If the ratio in the hypothesis is less than the ratio in the premise, it can be inferred as entailment
    label = "entailment"

print(label)
