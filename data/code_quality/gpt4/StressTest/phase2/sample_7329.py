# Variables for the ratios of red, green and blue bricks for premise and hypothesis
red_brick_ratio_premise = 4
green_brick_ratio_premise = 3
blue_brick_ratio_premise = 1

red_brick_ratio_hypothesis = 3
green_brick_ratio_hypothesis = 3
blue_brick_ratio_hypothesis = 1

# Comparing the ratios of red, green and blue bricks between premise and hypothesis
if red_brick_ratio_hypothesis > red_brick_ratio_premise:
    # Checking if the hypothesis contradicts the premise for the ratio of red bricks
    label = "contradiction"
elif green_brick_ratio_hypothesis != green_brick_ratio_premise or blue_brick_ratio_hypothesis != blue_brick_ratio_premise:
    # Checking if the hypothesis contradicts the premise for the ratio of green and blue bricks
    label = "contradiction"
elif red_brick_ratio_hypothesis <= red_brick_ratio_premise:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # If the hypothesis does not contradict the premise and cannot be explicitly entailed, it is neutral
    label = "neutral"

print(label)
