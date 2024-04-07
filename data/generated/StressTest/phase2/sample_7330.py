# Premise: Hali builds a tower using only red, green, and blue toy bricks in a ratio of more than 3:3:1.
# Hypothesis: Hali builds a tower using only red, green, and blue toy bricks in a ratio of 4:3:1.
# Golden Label: neutral

red_green_blue_ratio_premise = [3, 3, 1]
red_green_blue_ratio_hypothesis = [4, 3, 1]

# the hypothesis refers to the ratio of red, green, and blue toy bricks mentioned in the premise
if red_green_blue_ratio_hypothesis[0] <= red_green_blue_ratio_premise[0] or red_green_blue_ratio_hypothesis[1] != red_green_blue_ratio_premise[1] or red_green_blue_ratio_hypothesis[2] != red_green_blue_ratio_premise[2]:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif red_green_blue_ratio_hypothesis[0] > red_green_blue_ratio_premise[0] and red_green_blue_ratio_hypothesis[1] == red_green_blue_ratio_premise[1] and red_green_blue_ratio_hypothesis[2] == red_green_blue_ratio_premise[2]:
    # if the ratio in the hypothesis does not contradict the premise ratio, we can infer entailment
    label = "entailment"
else:
    # if the ratio in the hypothesis is not exactly the same as the ratio in the premise, it means that the relation is neutral
    label = "neutral"

print(label)

