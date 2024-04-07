# Premise: Lali builds a tower using only red, green, and blue toy bricks in a ratio of 4:3:1.
# Hypothesis: Lali builds a tower using only red, green, and blue toy bricks in a ratio of less than 7:3:1.
# Golden Label: entailment

# ratio of red, green and blue bricks in the premise
red_green_blue_ratio_premise = 4 / 3

# ratio of red, green and blue bricks in the hypothesis
red_green_blue_ratio_hypothesis = 7 / 3

# the hypothesis talks about the ratio of red, green and blue bricks, referenced also in the premise
if red_green_blue_ratio_hypothesis >= red_green_blue_ratio_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
else:
    # the premise gives a specific ratio for the bricks
    # any ratio of red, green, blue bricks less than 'red_green_blue_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

