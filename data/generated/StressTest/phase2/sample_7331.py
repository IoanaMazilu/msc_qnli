# Premise: Hali builds a tower using only red, green, and blue toy bricks in a ratio of 4:3:1.
# Hypothesis: Hali builds a tower using only red, green, and blue toy bricks in a ratio of less than 4:3:1.
# Golden Label: contradiction

red_green_blue_ratio_premise = (4, 3, 1)
red_green_blue_ratio_hypothesis = 'less than 4:3:1'

# the hypothesis refers to the ratio of red, green, and blue toy bricks used in Hali's tower mentioned in the premise
if red_green_blue_ratio_hypothesis == red_green_blue_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio for the colors of the toy bricks
    # any ratio less than 'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

